# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: OrderDesk
def undo_last_order():
    """Откат последних 3 операций: создание заказа, добавление позиции, оплата."""
    actions = [
        {"type": "create_order", "order_id": orders[-1]["id"], "client_id": orders[-1]["client_id"]},
        {"type": "add_item", "order_id": orders[-1]["id"], "item_id": items[-1]["id"], "price": items[-1]["price"]},
        {"type": "pay_order", "order_id": orders[-1]["id"], "payment_id": payments[-1]["id"], "amount": payments[-1]["amount"]}
    ]
    for action in actions:
        if action["type"] == "create_order":
            del orders[orders.index({"id": action["order_id"]})]
        elif action["type"] == "add_item":
            items.remove({"id": action["item_id"]})
        elif action["type"] == "pay_order":
            payments.remove({"id": action["payment_id"]})

    # Восстанавливаем статус заказа если нужно
    if orders:
        for order in orders:
            if order["status"] != "completed":
                order["status"] = "new"
