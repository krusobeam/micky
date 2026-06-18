# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: OrderDesk
class OrderDesk:
    def __init__(self):
        self.clients = {}
        self.items = []
        self.orders = []
        self.payments = []
        self.history = []

    def add_client(self, name, email):
        client_id = len(self.clients) + 1
        self.clients[client_id] = {"name": name, "email": email}
        return client_id

    def add_item(self, product_name, price):
        item_id = len(self.items) + 1
        self.items.append({"id": item_id, "product_name": product_name, "price": float(price)})
        return item_id

    def create_order(self, client_id, item_ids, status="new"):
        order_id = len(self.orders) + 1
        order = {
            "order_id": order_id,
            "client_id": client_id,
            "items": [item for item in self.items if item["id"] in item_ids],
            "status": status,
            "created_at": str(datetime.now())
        }
        self.orders.append(order)
        return order_id

    def add_payment(self, order_id, amount):
        payment_id = len(self.payments) + 1
        payment = {
            "payment_id": payment_id,
            "order_id": order_id,
            "amount": float(amount),
            "timestamp": str(datetime.now())
        }
        self.payments.append(payment)
        return payment_id

    def log_event(self, event_type, details):
        entry = {
            "event_type": event_type,
            "details": details,
            "timestamp": str(datetime.now())
        }
        self.history.append(entry)
