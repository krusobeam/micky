# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: OrderDesk
import json, uuid, datetime as dt
from dataclasses import dataclass, field, asdict
from typing import List, Optional

@dataclass
class Customer: id=uuid.uuid4().hex[:8]; name=""; email=""
@dataclass
class Item: sku; quantity; price
@dataclass
class OrderStatus: PENDING; CONFIRMED; SHIPPED; DELIVERED; CANCELLED
@dataclass
class Payment: method; amount; date=dt.datetime.now().isoformat()
@dataclass(order=True)
class OrderItem(OrderItem): id=uuid.uuid4().hex[:8]
@dataclass
class Order: number=f"ORD-{uuid.uuid4().hex[:6]}"; customer_id; items=list[OrderItem]; status=OrderStatus.PENDING; payments=list[Payment]; created_at=dt.datetime.now().isoformat()

def init_demo_data(db_path="orders.db"):
    db = {"customers": [], "orders": []}
    for i in range(3):
        c = Customer(id=f"CUST-{i+1:02d}", name=f"Клиент {i+1}", email=f"user{i}@example.com")
        db["customers"].append(c)
    for i in range(5):
        o = Order(customer_id=db["customers"][i % 3].id, items=[Item(sku="PROD-001", quantity=2, price=99.0), Item(sku="PROD-002", quantity=1, price=49.0)])
        db["orders"].append(o)
    with open(db_path, "w") as f: json.dump(db, f)

if __name__ == "__main__": init_demo_data()
