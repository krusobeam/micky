# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: OrderDesk
def generate_summary():
    print("=== СВОДКА ПО ЗАКАЗАМ ===")
    total_orders = len(orders)
    if not orders:
        print("Заказы отсутствуют.")
        return
    
    statuses = {}
    for order in orders:
        s = order['status']
        statuses[s] = statuses.get(s, 0) + 1
    
    revenue = sum(order['total_amount'] for order in orders if order['payment_status'] == 'paid')
    
    print(f"Всего заказов: {total_orders}")
    print(f"Выручка (оплачено): {revenue:.2f} руб.")
    print("Статусы:")
    for status, count in sorted(statuses.items()):
        print(f"  - {status}: {count}")
    
    if clients:
        active_clients = len([c for c in clients if any(o['client_id'] == c['id'] and o['status'] != 'cancelled' for o in orders)])
        print(f"Активные клиенты с заказами: {active_clients} из {len(clients)}")
