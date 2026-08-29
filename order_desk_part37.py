# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: OrderDesk
import unittest

class TestOrderDesk(unittest.TestCase):
    def test_order_creation(self):
        from orders import Order, OrderStatus
        order = Order("ORD-001", OrderStatus.NEW)
        self.assertEqual(order.status, OrderStatus.NEW)
        self.assertEqual(order.id, "ORD-001")

    def test_add_item(self):
        from orders import Order, OrderItem
        order = Order("ORD-002", OrderStatus.NEW)
        item = OrderItem("Widget", 10, 5)
        order.add_item(item)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.total(), 50)

    def test_add_payment(self):
        from orders import Order, Payment
        order = Order("ORD-003", OrderStatus.NEW)
        order.add_item(OrderItem("Gadget", 20, 3))
        payment = Payment("PAY-001", 60, "VISA")
        order.add_payment(payment)
        self.assertEqual(len(order.payments), 1)

    def test_status_transitions(self):
        from orders import Order, OrderStatus
        order = Order("ORD-004", OrderStatus.NEW)
        order.confirm()
        self.assertEqual(order.status, OrderStatus.CONFIRMED)
        order.ship()
        self.assertEqual(order.status, OrderStatus.SHIPPED)
        order.complete()
        self.assertEqual(order.status, OrderStatus.COMPLETED)

    def test_customer_creation(self):
        from orders import Customer
        cust = Customer("John", "john@example.com")
        self.assertEqual(cust.name, "John")
        self.assertEqual(len(cust.orders), 0)

    def test_order_linked_to_customer(self):
        from orders import Order, OrderStatus, Customer
        cust = Customer("Jane", "jane@example.com")
        order = Order("ORD-005", OrderStatus.NEW)
        order.customer = cust
        self.assertEqual(order.customer, cust)

    def test_history_log(self):
        from orders import Order, OrderStatus
        order = Order("ORD-006", OrderStatus.NEW)
        order.confirm()
        order.ship()
        self.assertEqual(len(order.history), 2)

if __name__ == "__main__":
    unittest.main()
