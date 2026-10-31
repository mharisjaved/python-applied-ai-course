"""The ONE place where the app uses AI: turn category totals into a short summary and two tips.

write_summary(totals, ask=ask_llm)
  1. build a prompt that contains ONLY the totals (no dates, no descriptions)
  2. ask the model (real Claude, or the offline mock)
  3. parse and check the JSON reply
  4. if anything goes wrong, fall back to the Day 57 template, so the app never crashes
"""

import json

import anthropic

from llm import REFUSAL_MESSAGE, ask_llm, mock_llm
from spending import FIXED_COSTS, top_categories

TIPS = {
    "food": "Plan a few meals ahead and cook in batches; eating out adds up fast.",
    "transport": "Compare a monthly pass with what you paid for single tickets and taxis.",
    "entertainment": "Pick one or two paid activities per week and look for free events.",
    "shopping": "Wait 48 hours before buying anything that is not essential.",
    "health": "Check whether your student card gives discounts at pharmacies or the dentist.",
}
GENERAL_TIP = "Check your spending once a week, not only at the end of the month."


def template_summary(totals):
    """The Day 57 non-AI version. Now it is the fallback when the model's reply is unusable."""
    total = sum(totals.values())
    biggest, biggest_amount = top_categories(totals, n=1)[0]
    summary = f"You spent {total:.2f} in total. The biggest category was {biggest} ({biggest_amount:.2f})."
    tips = []
    for category, amount in top_categories(totals, n=2, skip_fixed=True):
        tips.append(TIPS.get(category, GENERAL_TIP))
    while len(tips) < 2:
        tips.append(GENERAL_TIP)
    return {"summary": summary, "tips": tips}


def build_prompt(totals):
    """The prompt contains ONLY category totals: no dates, no descriptions, nothing personal."""
    lines = []
    for category, amount in top_categories(totals, n=len(totals)):
        note = ""
        if category in FIXED_COSTS:
            note = " (fixed)"
        lines.append(f"- {category}: {amount:.2f}{note}")
    return (
        "You are a friendly budgeting helper for students. Give simple, general budgeting tips,\n"
        "never investment or financial-product advice.\n\n"
        "Here are a student's spending totals for one month, by category, biggest first:\n"
        + "\n".join(lines)
        + f"\nTotal: {sum(totals.values()):.2f}\n\n"
        "Write a summary of at most two sentences and exactly two practical tips.\n"
        "Tips must be about categories that are NOT marked (fixed).\n"
        "Only use numbers that appear above. Do not invent amounts or percentages.\n"
        'Reply with JSON only, in this shape: {"summary": "...", "tips": ["...", "..."]}'
    )


def parse_summary(reply):
    """Return {"summary": text, "tips": [text, text]}, or None if the reply is not usable."""
    text = reply.strip()
    if text.startswith("```"):  # some models wrap JSON in a ```json ... ``` code fence
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:]
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    summary = data.get("summary")
    tips = data.get("tips")
    if not isinstance(summary, str) or summary.strip() == "":
        return None
    if not isinstance(tips, list) or len(tips) != 2:
        return None
    for tip in tips:
        if not isinstance(tip, str) or tip.strip() == "":
            return None
    return {"summary": summary.strip(), "tips": [tip.strip() for tip in tips]}


def call_model(prompt, ask):
    """Ask the model. If the API fails (key, limits, network), let the offline mock answer instead."""
    try:
        return ask(prompt)
    except anthropic.AuthenticationError:
        print("(The API key was rejected, so the offline mock answered. Check your .env file.)")
    except anthropic.RateLimitError:
        print("(Too many requests right now, so the offline mock answered.)")
    except anthropic.APIConnectionError:
        print("(No connection to the API, so the offline mock answered.)")
    except anthropic.APIStatusError as error:
        print(f"(The API returned error {error.status_code}, so the offline mock answered.)")
    return mock_llm(prompt)


def write_summary(totals, ask=ask_llm):
    """The ONE AI function. Always returns {"summary", "tips", "source"} and never crashes.

    Tests pass their own fake `ask` function, so they never need the network.
    """
    prompt = build_prompt(totals)
    reply = call_model(prompt, ask)
    if reply == REFUSAL_MESSAGE:
        result = template_summary(totals)
        result["source"] = "template (the model declined)"
        return result
    result = parse_summary(reply)
    if result is None:
        result = template_summary(totals)
        result["source"] = "template (the reply was not valid JSON)"
        return result
    result["source"] = "ai"
    return result
