"""Tests for the AI part of the spending app. Run from this folder:  uv run pytest -q

No test calls the real API: fake `ask` functions play the model, and COURSE_OFFLINE=1 is set
so that even the default ask_llm uses the mock.
"""

import json
import os

from llm import REFUSAL_MESSAGE
from summary import build_prompt, parse_summary, write_summary

os.environ["COURSE_OFFLINE"] = "1"

TOTALS = {"rent": 650.0, "food": 20.0, "transport": 3.0}
GOOD_REPLY = json.dumps({"summary": "You spent 673.00, mostly on rent.",
                         "tips": ["Cook at home more often.", "Walk short distances."]})


# ---------- fake models: each one plays a different kind of reply ----------

def fake_good(prompt):
    return GOOD_REPLY


def fake_chatty(prompt):
    return "Sure! Here is your summary: you spent a lot on rent."


def fake_refusal(prompt):
    return REFUSAL_MESSAGE


def fake_fenced(prompt):
    return "```json\n" + GOOD_REPLY + "\n```"


# ---------- prompt ----------

def test_prompt_contains_totals_marks_fixed_costs_and_asks_for_json():
    prompt = build_prompt(TOTALS)
    assert "- rent: 650.00 (fixed)" in prompt
    assert "- food: 20.00" in prompt
    assert "Total: 673.00" in prompt
    assert "JSON" in prompt


# ---------- parsing ----------

def test_parse_summary_accepts_good_json():
    assert parse_summary(GOOD_REPLY)["tips"] == ["Cook at home more often.", "Walk short distances."]


def test_parse_summary_rejects_unusable_replies():
    assert parse_summary("not json at all") is None
    assert parse_summary('["a list", "not a dict"]') is None
    assert parse_summary('{"summary": "ok", "tips": ["only one tip"]}') is None
    assert parse_summary('{"tips": ["a", "b"]}') is None


# ---------- the AI boundary ----------

def test_good_reply_is_used():
    result = write_summary(TOTALS, ask=fake_good)
    assert result["source"] == "ai"
    assert result["summary"] == "You spent 673.00, mostly on rent."


def test_chatty_reply_falls_back_to_template():
    result = write_summary(TOTALS, ask=fake_chatty)
    assert result["source"] == "template (the reply was not valid JSON)"
    assert len(result["tips"]) == 2


def test_refusal_falls_back_to_template():
    result = write_summary(TOTALS, ask=fake_refusal)
    assert result["source"] == "template (the model declined)"


def test_json_inside_a_code_fence_is_still_accepted():
    assert write_summary(TOTALS, ask=fake_fenced)["source"] == "ai"


def test_offline_mock_gives_a_valid_summary():
    result = write_summary(TOTALS)  # default ask_llm -> offline -> mock_llm
    assert result["source"] == "ai"
    assert "food" in result["summary"]
    assert "673.00" in result["summary"]
