# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: OrderDesk
def get_weekly_stats():
    """Calculate weekly order statistics grouped by ISO week."""
    from collections import defaultdict
    weeks = defaultdict(lambda: {"orders": 0, "amount": 0.0, "completed": 0})
    for o in orders:
        w = o.date.isocalendar()[:2]
        weeks[w]["orders"] += 1
        if o.status == STATUS_COMPLETED:
            weeks[w]["completed"] += 1
        else:
            weeks[w]["amount"] += float(o.total)
    return [{"week": list(k), "orders": v["orders"], "completed": v["completed"], "revenue": round(v["amount"], 2)} for k, v in sorted(weeks.items())]
