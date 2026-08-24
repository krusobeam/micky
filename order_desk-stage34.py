# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: OrderDesk
TEMPLATES = {
    "order": {
        "status": "pending",
        "items": [],
        "notes": "",
        "payment_method": "cash",
    },
    "customer": {
        "name": "",
        "email": "",
        "phone": "",
        "address": "",
    },
    "payment": {
        "amount": 0,
        "method": "cash",
        "notes": "",
    },
    "item": {
        "name": "",
        "quantity": 1,
        "price": 0,
    },
}

def create_from_template(template_name, **overrides):
    """Создать запись из шаблона, применив пользовательские оверрайды."""
    if template_name not in TEMPLATES:
        raise ValueError(f"Неизвестный шаблон: {template_name}")
    record = TEMPLATES[template_name].copy()
    record.update(overrides)
    return record

if __name__ == "__main__":
    new_order = create_from_template("order", status="urgent", notes="Срочно")
    print(new_order)
    new_customer = create_from_template("customer", name="Иван", phone="12345")
    print(new_customer)
