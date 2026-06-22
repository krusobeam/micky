# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: OrderDesk
def handle_deletion(entity_type, entity_id):
    if not isinstance(entity_id, int) or entity_id <= 0:
        print(f"Ошибка: Неверный ID для удаления {entity_type} ({entity_id}).")
        return False
    
    try:
        if entity_type == "clients":
            del clients[entity_id]
            print(f"Клиент #{entity_id} успешно удален.")
        elif entity_type == "orders":
            del orders[entity_id]
            for order in list(orders.values()):
                if order['id'] == entity_id:
                    del order['items'][0]
                    break
            print(f"Заказ #{entity_id} успешно удален.")
        elif entity_type == "payments":
            del payments[entity_id]
            for payment in list(payments.values()):
                if payment['id'] == entity_id:
                    del payment['order_items'][0]
                    break
            print(f"Оплата #{entity_id} успешно удалена.")
        elif entity_type == "statuses":
            del statuses[entity_id]
            for status in list(statuses.values()):
                if status['id'] == entity_id:
                    del status['history'][0]
                    break
            print(f"Статус #{entity_id} успешно удален.")
        else:
            print(f"Неизвестный тип сущности для удаления: {entity_type}.")
            return False
        
        return True
    except KeyError:
        print(f"Ошибка: Сущность {entity_type} с ID {entity_id} не найдена.")
        return False

# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: OrderDesk
def delete_record(table_name, record_id):
    if not table_name or not record_id:
        raise ValueError("Идентификатор таблицы и записи обязательны")
    
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        return cursor.rowcount > 0
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            raise ValueError(f"Таблица '{table_name}' не найдена")
        raise
