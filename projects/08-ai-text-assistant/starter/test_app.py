"""Tests for the Review Insights Assistant (Must requirements).

Most of them fail until you finish the TODOs in app.py. That is expected: make them pass one TODO at a time.
No test calls the real API: each one passes a mock model.

Run from this folder:  uv run pytest -q
"""

import pytest

from app import analyse_all, build_prompt, load_reviews, make_report, parse_response, redact
from llm import mock_llm

GOOD_REPLY = '{"sentiment": "negative", "topics": ["quality"], "summary": "The zip broke."}'


class RecordingModel:
    """A mock model that remembers every prompt it receives and answers like mock_llm."""

    def __init__(self):
        self.prompts = []

    def ask(self, prompt):
        self.prompts.append(prompt)
        return mock_llm(prompt)


class FlakyModel:
    """A mock model whose first reply is not JSON; after that it answers like mock_llm."""

    def __init__(self):
        self.calls = 0

    def ask(self, prompt):
        self.calls += 1
        if self.calls == 1:
            return "Sorry, I am not sure."
        return mock_llm(prompt)


def broken_model(prompt):
    """A mock model that never gives a usable reply."""
    return "I would rather not answer in JSON today."


# --- load_reviews -------------------------------------------------------------------------------

def test_load_reviews_reads_all_40_reviews():
    reviews = load_reviews()
    assert len(reviews) == 40
    assert reviews[0]["review_id"] == "R01"
    assert reviews[0]["product"] == "wireless earbuds"


def test_load_reviews_converts_rating_to_int():
    for review in load_reviews():
        assert isinstance(review["rating"], int)


# --- redact -------------------------------------------------------------------------------------

def test_redact_replaces_email():
    assert redact("Write to jo.example@example.com today") == "Write to [EMAIL] today"


def test_redact_replaces_phone_and_keeps_punctuation():
    assert redact("Call me at 555-0142.") == "Call me at [PHONE]."


def test_redact_keeps_normal_numbers_and_text():
    text = "No blisters after 10 km. Sole peeled after 100 km."
    assert redact(text) == text


def test_redact_review_r33():
    r33 = [review for review in load_reviews() if review["review_id"] == "R33"][0]
    clean = redact(r33["review_text"])
    assert "@" not in clean
    assert "555-0142" not in clean
    assert "[EMAIL]" in clean and "[PHONE]" in clean


# --- build_prompt -------------------------------------------------------------------------------

def test_build_prompt_puts_review_inside_tags_and_asks_for_json():
    prompt = build_prompt("backpack", "Zip broke within a month.")
    assert "<review>" in prompt and "</review>" in prompt
    assert "Zip broke within a month." in prompt
    assert "JSON" in prompt
    assert "backpack" in prompt


def test_build_prompt_never_contains_personal_data():
    prompt = build_prompt("backpack", "Call 555-0142 or email jo.example@example.com")
    assert "555-0142" not in prompt
    assert "jo.example@example.com" not in prompt


# --- parse_response -----------------------------------------------------------------------------

def test_parse_response_accepts_json_with_text_around_it():
    reply = "Here you go:\n```json\n" + GOOD_REPLY + "\n```"
    assert parse_response(reply) == {"sentiment": "negative", "topics": ["quality"], "summary": "The zip broke."}


def test_parse_response_cleans_values():
    reply = '{"sentiment": " Mixed", "topics": ["Battery ", "Sound"], "summary": " Okay. "}'
    assert parse_response(reply) == {"sentiment": "mixed", "topics": ["battery", "sound"], "summary": "Okay."}


def test_parse_response_rejects_text_without_json():
    with pytest.raises(ValueError):
        parse_response("I think it is positive.")


def test_parse_response_rejects_label_that_is_not_allowed():
    with pytest.raises(ValueError):
        parse_response('{"sentiment": "neutral", "topics": [], "summary": "Fine."}')


def test_parse_response_rejects_missing_key():
    with pytest.raises(ValueError):
        parse_response('{"sentiment": "positive", "summary": "Fine."}')


def test_parse_response_rejects_topics_that_are_not_a_list():
    with pytest.raises(ValueError):
        parse_response('{"sentiment": "positive", "topics": "battery", "summary": "Fine."}')


# --- analyse_all --------------------------------------------------------------------------------

def test_analyse_all_with_the_mock_model():
    reviews = load_reviews()[:5]
    results, failed_ids = analyse_all(reviews, ask=mock_llm)
    assert failed_ids == []
    assert len(results) == 5
    assert results[0]["review_id"] == "R01"
    assert results[0]["sentiment"] == "positive"
    assert results[0]["rating"] == 5


def test_analyse_all_counts_failures_without_crashing():
    reviews = load_reviews()[:3]
    results, failed_ids = analyse_all(reviews, ask=broken_model)
    assert results == []
    assert failed_ids == ["R01", "R02", "R03"]


def test_analyse_all_retries_once_after_an_unusable_reply():
    model = FlakyModel()
    results, failed_ids = analyse_all(load_reviews()[:1], ask=model.ask)
    assert failed_ids == []
    assert len(results) == 1
    assert model.calls == 2


def test_analyse_all_never_sends_personal_data_to_the_model():
    model = RecordingModel()
    analyse_all(load_reviews(), ask=model.ask)
    assert len(model.prompts) == 40
    for prompt in model.prompts:
        assert "@" not in prompt
        assert "555-0142" not in prompt


# --- make_report --------------------------------------------------------------------------------

def make_results():
    return [
        {"review_id": "R11", "product": "backpack", "rating": 5, "sentiment": "positive",
         "topics": ["comfort"], "summary": "Fits a laptop."},
        {"review_id": "R13", "product": "backpack", "rating": 2, "sentiment": "negative",
         "topics": ["quality", "design"], "summary": "Zip broke."},
        {"review_id": "R09", "product": "coffee maker", "rating": 5, "sentiment": "negative",
         "topics": ["quality", "delivery"], "summary": "Cracked jug."},
    ]


def test_make_report_shows_totals_and_failures():
    report = make_report(make_results(), ["R05"])
    assert "Reviews analysed: 3 (failed: 1)" in report


def test_make_report_counts_sentiment_per_product():
    report = make_report(make_results(), [])
    assert "backpack: positive 1, negative 1, mixed 0" in report
    assert "coffee maker: positive 0, negative 1, mixed 0" in report


def test_make_report_lists_most_common_topics():
    report = make_report(make_results(), [])
    assert "quality: 2" in report
