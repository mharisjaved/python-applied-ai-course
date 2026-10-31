"""Tests for review_analyser.py. They never call the real API: every test uses a mock.

Run them from this folder:  uv run pytest -q
"""

import pytest

from mock_model import MockLLM
from review_analyser import analyse_review, parse_json_reply, validate_analysis

GOOD_REPLY = '{"sentiment": "negative", "topics": ["quality"], "summary": "The zip broke."}'


# --- parse_json_reply --------------------------------------------------------------------------

def test_parse_plain_json():
    assert parse_json_reply(GOOD_REPLY)["sentiment"] == "negative"


def test_parse_json_with_text_and_code_fence_around_it():
    reply = "Here is the analysis:\n```json\n" + GOOD_REPLY + "\n```"
    assert parse_json_reply(reply)["topics"] == ["quality"]


def test_parse_reply_without_json_raises():
    with pytest.raises(ValueError):
        parse_json_reply("Sure! I think this review is negative.")


def test_parse_broken_json_raises():
    with pytest.raises(ValueError):
        parse_json_reply('{"sentiment": "negative",}')


# --- validate_analysis -------------------------------------------------------------------------

def test_validate_cleans_the_values():
    data = {"sentiment": " Positive ", "topics": ["Battery ", "SOUND"], "summary": " Great. "}
    assert validate_analysis(data) == {"sentiment": "positive", "topics": ["battery", "sound"],
                                       "summary": "Great."}


def test_validate_keeps_at_most_three_topics():
    data = {"sentiment": "mixed", "topics": ["a", "b", "c", "d"], "summary": "Fine."}
    assert validate_analysis(data)["topics"] == ["a", "b", "c"]


def test_validate_rejects_missing_key():
    with pytest.raises(ValueError):
        validate_analysis({"sentiment": "positive", "topics": []})


def test_validate_rejects_label_that_is_not_allowed():
    with pytest.raises(ValueError):
        validate_analysis({"sentiment": "neutral", "topics": [], "summary": "Okay."})


def test_validate_rejects_topics_that_are_not_a_list():
    with pytest.raises(ValueError):
        validate_analysis({"sentiment": "positive", "topics": "battery", "summary": "Okay."})


def test_validate_rejects_empty_summary():
    with pytest.raises(ValueError):
        validate_analysis({"sentiment": "positive", "topics": [], "summary": "   "})


# --- analyse_review with a mock model ----------------------------------------------------------

def test_analyse_works_on_the_first_try():
    model = MockLLM()
    result = analyse_review("The zip broke after a week.", ask=model.ask)
    assert result["sentiment"] == "negative"
    assert model.calls == 1


def test_analyse_retries_once_with_a_stricter_prompt():
    model = MockLLM(fail_first=1)
    result = analyse_review("Love it! Easy to clean.", ask=model.ask)
    assert result["sentiment"] == "positive"
    assert model.calls == 2
    assert "ONLY" in model.prompts[1]


def test_analyse_gives_up_after_two_bad_replies():
    model = MockLLM(fail_first=5)
    assert analyse_review("Love it!", ask=model.ask) is None
    assert model.calls == 2


def test_analyse_retries_when_the_label_is_not_allowed():
    model = MockLLM(fail_first=1, bad_reply='{"sentiment": "neutral", "topics": [], "summary": "Ok."}')
    result = analyse_review("Sound is great, battery is terrible.", ask=model.ask)
    assert result["sentiment"] == "mixed"
