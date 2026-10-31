"""The ONE place where the app will use AI.

Day 57: no AI yet. write_summary() fills a simple template, so the whole app already works end to end.
Day 58: the inside of write_summary() changes to call a model; nothing else in the app has to change.
"""

from spending import top_categories

TIPS = {
    "food": "Plan a few meals ahead and cook in batches; eating out adds up fast.",
    "transport": "Compare a monthly pass with what you paid for single tickets and taxis.",
    "entertainment": "Pick one or two paid activities per week and look for free events.",
    "shopping": "Wait 48 hours before buying anything that is not essential.",
    "health": "Check whether your student card gives discounts at pharmacies or the dentist.",
}
GENERAL_TIP = "Check your spending once a week, not only at the end of the month."


def write_summary(totals):
    """Return {"summary": text, "tips": [tip, tip]} for a dict of category totals."""
    total = sum(totals.values())
    biggest, biggest_amount = top_categories(totals, n=1)[0]
    summary = f"You spent {total:.2f} in total. The biggest category was {biggest} ({biggest_amount:.2f})."
    tips = []
    for category, amount in top_categories(totals, n=2, skip_fixed=True):
        tips.append(TIPS.get(category, GENERAL_TIP))
    while len(tips) < 2:
        tips.append(GENERAL_TIP)
    return {"summary": summary, "tips": tips}
