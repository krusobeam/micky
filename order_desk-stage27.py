# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: OrderDesk
def reset_demo_data():
    """Заполнить все коллекции тестовыми данными для быстрого старта."""
    global customers, products, orders, payments, statuses, order_history
    import datetime as dt
    
    customers = [
        {"id": "c1", "name": "Алексей Иванов", "phone": "+79001234567"},
        {"id": "c2", "name": "Мария Петрова", "phone": "+79007654321"},
        {"id": "c3", "name": "Дмитрий Сидоров", "phone": "+79001112233"},
    ]
    
    products = [
        {"id": "p1", "title": "Ноутбук Pro 15", "price": 89990},
        {"id": "p2", "title": "Клавиатура механическая", "price": 7500},
        {"id": "p3", "title": "Монитор 4K 27\"", "price": 32000},
    ]
    
    statuses = ["new", "confirmed", "processing", "shipped", "delivered"]
    
    orders = []
    payments = []
    order_history = []
    
    # Создаём пару示例 заказов
    sample_orders = [
        {"id": "o1", "customer_id": "c1", "items": [{"product_id": "p1", "qty": 1}], 
         "status": "delivered", "total": 89990, 
         "created_at": dt.datetime(2024, 3, 15, 10, 30)},
        {"id": "o2", "customer_id": "c2", "items": [{"product_id": "p2", "qty": 2}], 
         "status": "processing", "total": 15000,
         "created_at": dt.datetime(2024, 3, 16, 14, 0)},
    ]
    
    for order in sample_orders:
        orders.append(order)
        payments.append({"order_id": order["id"], "amount": order["total"], "paid": True})
        status_name = order["status"] if order["status"] != "confirmed" else "new"
        order_history.append({
            "timestamp": order["created_at"],
            "action": f"Заказ {order['id']} создан",
            "detail": {"customer_id": order["customer_id"]}
        })

def clear_all():
    """Полностью очистить все данные и коллекции."""
    global customers, products, orders, payments, statuses, order_history
    import datetime as dt
    
    customers = []
    products = []
    orders = []
    payments = []
    order_history = []
    
    # Сохраняем статусы как неизменяемые
    statuses = ["new", "confirmed", "processing", "shipped", "delivered"]
