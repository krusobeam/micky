# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: OrderDesk
class OrderModel:
    def __init__(self):
        self.clients = {}
        self.items = {}
        self.orders = []
        self.payments = []
    
    def validate_client(self, name: str) -> tuple[bool, str]:
        if not name or len(name.strip()) < 2:
            return False, "Имя клиента должно содержать минимум 2 символа"
        existing = [c for c in self.clients.values() if c['name'].lower() == name.lower()]
        if existing and 'id' not in existing[0]:
            return True, f"Клиент '{name}' уже существует (ID: {existing[0]['id']})"
        return True, ""

    def validate_item(self, name: str, price: float) -> tuple[bool, str]:
        if not name or len(name.strip()) < 2:
            return False, "Название позиции должно содержать минимум 2 символа"
        if price <= 0:
            return False, "Цена должна быть положительным числом"
        existing = [i for i in self.items.values() if i['name'].lower() == name.lower()]
        if existing and 'id' not in existing[0]:
            return True, f"Позиция '{name}' уже существует (ID: {existing[0]['id']})"
        return True, ""

    def validate_order(self, client_id: int, item_ids: list[int], status: str) -> tuple[bool, str]:
        if not isinstance(item_ids, list) or len(item_ids) == 0:
            return False, "Список позиций заказа не может быть пустым"
        for iid in item_ids:
            if iid not in self.items:
                return False, f"Позиция с ID {iid} не найдена в системе"
        valid_statuses = ['created', 'processing', 'shipped', 'delivered', 'cancelled']
        if status not in valid_statuses:
            return False, f"Неверный статус. Доступные: {', '.join(valid_statuses)}"
        client_found = any(c['id'] == client_id for c in self.clients.values())
        if not client_found:
            return False, "Клиент не найден в системе"
        return True, ""

    def validate_payment(self, order_id: int, amount: float) -> tuple[bool, str]:
        if amount <= 0:
            return False, "Сумма оплаты должна быть положительной"
        order = next((o for o in self.orders if o['id'] == order_id), None)
        if not order:
            return False, "Заказ не найден"
        total_paid = sum(p['amount'] for p in self.payments if p['order_id'] == order_id)
        if amount + total_paid > order.get('total_amount', 0):
            return False, f"Сумма оплаты превышает стоимость заказа ({order.get('total_amount')})"
        return True, ""
