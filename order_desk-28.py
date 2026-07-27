# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: OrderDesk
import statistics
from collections import Counter, defaultdict


def calculate_metrics(orders):
    """Calculate key KPIs for the OrderDesk system."""
    if not orders:
        return {
            "total_orders": 0,
            "unique_customers": 0,
            "completion_rate": 0.0,
            "avg_revenue_per_order": 0.0,
            "top_status": None,
            "revenue_by_month": {},
        }

    total = len(orders)
    unique_customers = len(set(order["customer"] for order in orders))
    completed = sum(1 for o in orders if o.get("status") == "completed")
    completion_rate = (completed / total * 100) if total else 0.0

    revenues = [sum(item["price"] * item["qty"] for item in order.get("items", [])) for order in orders]
    avg_revenue = sum(revenues) / len(revenues) if revenues else 0.0

    status_counts = Counter(o.get("status") for o in orders)
    top_status = status_counts.most_common(1)[0][0] if status_counts else None

    revenue_by_month = defaultdict(float)
    for order in orders:
        month_key = order.get("month", "unknown")
        revenue_by_month[month_key] += sum(item["price"] * item["qty"] for item in order.get("items", []))

    return {
        "total_orders": total,
        "unique_customers": unique_customers,
        "completion_rate": round(completion_rate, 2),
        "avg_revenue_per_order": round(avg_revenue, 2),
        "top_status": top_status,
        "revenue_by_month": dict(revenue_by_month),
    }


metrics = calculate_metrics(orders)
print("=== OrderDesk KPIs ===")
for k, v in metrics.items():
    print(f"{k}: {v}")
