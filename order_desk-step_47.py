# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: OrderDesk
def demo():
    print("=== OrderDesk Demo ===")
    client = Client("Иванов Иван")
    client.add_item("Ноутбук", 50000)
    client.add_item("Мышь", 1500)
    client.add_item("Клавиатура", 3000)
    order = client.create_order()
    order.set_status("Ожидает оплаты")
    order.pay(55000)
    order.set_status("Выполнен")
    for entry in order.history:
        print(f"  {entry}")
    print(f"  Итого: {order.total}")
    print("=== Конец демо ===")
