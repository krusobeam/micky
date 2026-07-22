# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: OrderDesk
def print_order_record(order: Order) -> None:
    """Компактный вывод одной записи заказа с ключевыми деталями."""
    status_map = {s: v for v, s in STATUS.items()}
    lines = [f"--- Заказ #{order.id} ---"]
    lines.append(f"Клиент: {order.client_name or order.client_id}")
    lines.append(f"Статус: {status_map.get(order.status, order.status)}")
    if order.created_at:
        lines.append(f"Дата создания: {order.created_at}")
    if order.completed_at:
        lines.append(f"Завершён: {order.completed_at}")

    subtotal = sum(p.price * p.quantity for p in order.items)
    tax_rate = TAX_RATE if order.tax_applied else 0.0
    total = subtotal + (subtotal * tax_rate) if order.tax_applied else subtotal
    discount = order.discount or 0
    final_total = total - discount

    lines.append(f"Позиций: {len(order.items)}")
    for item in order.items:
        lines.append(
            f"  [{item.id}] {item.product_name} x{item.quantity} @ {item.price}"
        )

    if order.payment_history:
        lines.append("Оплата:")
        for p in order.payment_history:
            lines.append(f"  - {p.method} {p.amount} ({p.status})")

    lines.append(f"Итого: {final_total:.2f}")
    print("\n".join(lines))
