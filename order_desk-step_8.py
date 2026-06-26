# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: OrderDesk
def main():
    while True:
        print("\n=== OrderDesk CLI ===")
        print("1. Список клиентов | 2. Добавить клиента | 3. Создать заказ | 4. Оплатить заказ | 5. История заказов | 6. Выход")
        try:
            choice = input("Выберите действие (1-6): ").strip()
        except KeyboardInterrupt:
            print("\n\nВыход из системы.")
            break
        
        if choice == "1":
            for c in clients.values():
                print(f"ID:{c['id']} | Имя:{c['name']}")
        elif choice == "2":
            name = input("Имя клиента: ").strip() or "Аноним"
            clients[next_id] = {"id": next_id, "name": name}
            print(f"Клиент {name} добавлен (ID={next_id})")
        elif choice == "3":
            if not clients:
                print("Нет клиентов.")
                continue
            cid = input("ID клиента (или имя): ").strip() or next(iter(clients))
            items_str = input("Позиции (напр. '1xApple, 2xBread'): ").strip()
            status = "new"
            orders[next_order_id] = {"id": next_order_id, "client": clients[cid]["name"], "items": parse_items(items_str), "status": status}
        elif choice == "4":
            if not orders:
                print("Нет заказов.")
                continue
            oid = input("ID заказа (или имя): ").strip() or next(iter(orders))
            pay_amount = float(input("Сумма оплаты: "))
            order = orders[oid]
            if order["status"] == "new":
                order["status"] = "paid"
                print(f"Заказ {order['id']} оплачен.")
        elif choice == "5":
            for o in sorted(orders.values(), key=lambda x: x.get("created_at", 0), reverse=True):
                print(f"[{o['status']}] Заказ #{o['id']} от клиента {o['client']}: {', '.join(o['items'])}")
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
