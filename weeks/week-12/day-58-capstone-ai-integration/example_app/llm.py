"""Talk to Claude, or to an offline mock when there is no API key.

Online:  put ANTHROPIC_API_KEY=... in a .env file (copy .env.example from the course root).
Offline: no key, or COURSE_OFFLINE=1  ->  mock_llm() answers instead (free, instant, predictable).
"""

import json
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()  # read .env now, so LLM_MODEL below can also come from the .env file
MODEL = os.environ.get("LLM_MODEL", "claude-opus-5-5")
REFUSAL_MESSAGE = "[The model declined this request.]"


def llm_mode():
    """Say who will answer, so the user (and the audience at a demo) always knows."""
    if os.environ.get("COURSE_OFFLINE") == "1" or not os.environ.get("ANTHROPIC_API_KEY"):
        return "offline mock"
    return f"online ({MODEL})"


def mock_llm(prompt):
    """Offline stand-in for the model, written for THIS app's prompt.

    It reads the "- category: amount" lines and the "Total:" line from the prompt and
    replies in the JSON shape the real model is asked for, reusing the prompt's own numbers.
    """
    flexible = []  # (category, amount text) for categories not marked (fixed)
    total = "?"
    for line in prompt.splitlines():
        if line.startswith("- ") and ": " in line and "(fixed)" not in line:
            category, amount = line[2:].split(": ")
            flexible.append((category, amount))
        elif line.startswith("Total: "):
            total = line[len("Total: "):]
    if not flexible:
        return json.dumps({"summary": f"You spent {total} in total.",
                           "tips": ["Write down every expense for a week.", "Set a simple weekly limit."]})
    top, top_amount = flexible[0]  # the prompt lists categories biggest first
    second = top
    if len(flexible) > 1:
        second = flexible[1][0]
    return json.dumps({
        "summary": f"You spent {total} in total. Your biggest flexible category was {top} at {top_amount}.",
        "tips": [f"Set a weekly limit for {top} and check it every Sunday.",
                 f"Look at {second} next: small savings there add up over a month."],
    })


def ask_llm(prompt, system="You are a helpful assistant."):
    """Send one prompt to Claude and return its text reply (mock reply when offline)."""
    load_dotenv()  # reads ANTHROPIC_API_KEY from a .env file if present
    if os.environ.get("COURSE_OFFLINE") == "1" or not os.environ.get("ANTHROPIC_API_KEY"):
        return mock_llm(prompt)
    client = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY automatically
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # if this model declines, the API retries on a suitable fallback model
    )
    if response.stop_reason == "refusal":
        return REFUSAL_MESSAGE
    # The reply is a list of blocks (thinking blocks may come first), so keep only the text blocks.
    return "".join(block.text for block in response.content if block.type == "text")
