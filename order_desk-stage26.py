# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: OrderDesk
def run_demo():
    print("=== OrderDesk Demo ===")
    for cmd in [
        "create_client(name='Alice', phone='+1234567890')",
        "create_client(name='Bob', phone='+0987654321')",
        "add_item(item_id=1, name='Widget', price=9.99)",
        "add_item(item_id=2, name='Gadget', price=19.99)",
        "create_order(client_id=1, item_ids=[1], qty=[3])",
        "create_order(client_id=2, item_ids=[2], qty=[5])",
        "pay(order_id=1, amount=29.97, method='credit_card')",
        "pay(order_id=2, amount=99.95, method='bank_transfer')",
        "cancel_order(order_id=2)",
        "list_orders(status='completed')",
        "get_history()",
    ]:
        print(f"\n>>> {cmd}")
        try:
            exec(cmd)
        except Exception as e:
            print(f"  Error: {e}")
