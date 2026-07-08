# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: OrderDesk
import datetime as dt


def monthly_report(db):
    """Выводит месячную статистику заказов."""
    print("\n=== Месячная статистика ===")
    months = sorted(set(d.month for d in db["orders"].keys()))
    for m in months:
        month_orders = [k for k, v in db["orders"].items() if dt.datetime.strptime(k, "%Y-%m").month == m]
        if not month_orders:
            continue
        total_revenue = sum(
            float(db["orders"][o]["total"]) for o in month_orders if db["orders"][o]["status"] == "completed"
        )
        print(f"{dt.date.fromtimestamp(float(months.pop() * 100)).month:02d}: {len(month_orders)} заказов, выручка = {total_revenue:.2f}")
