# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: OrderDesk
def export_state_to_json():
    import json
    state = {
        "clients": list(clients.values()),
        "positions": list(positions.values()),
        "orders": list(orders.values()),
        "payments": list(payments.values())
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
