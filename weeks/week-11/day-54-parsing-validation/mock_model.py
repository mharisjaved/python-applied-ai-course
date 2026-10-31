"""A pretend model for tests: it answers predictably, and it can misbehave on purpose.

    model = MockLLM(fail_first=1)        # the first reply is broken, the next ones are fine
    result = analyse_review("Love it!", ask=model.ask)
    print(model.calls)                    # 2: one broken reply, then one retry
"""

from llm import mock_llm


class MockLLM:
    """Answers like mock_llm(), except that the first `fail_first` replies are `bad_reply`."""

    def __init__(self, fail_first=0, bad_reply="Sure! I think this review is positive."):
        self.fail_first = fail_first
        self.bad_reply = bad_reply
        self.calls = 0
        self.prompts = []

    def ask(self, prompt):
        """Record the prompt and return a reply (a broken one for the first `fail_first` calls)."""
        self.calls += 1
        self.prompts.append(prompt)
        if self.calls <= self.fail_first:
            return self.bad_reply
        return mock_llm(prompt)

    def __str__(self):
        return f"MockLLM(fail_first={self.fail_first}, calls so far={self.calls})"
