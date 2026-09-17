# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: OrderDesk
def self_check(app):
    print("=== Самопроверка OrderDesk ===")
    for c in app.clients:
        print(f"Клиент: {c.name}")
    for o in app.orders:
        print(f"Заказ #{o.id}: статус={o.status}, сумма={o.total}, позиции={o.items}")
    print("=== Самопроверка завершена ===")
