# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: OrderDesk
def edit_record(record_id, field_name, new_value):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    current_record = records[record_id]
    
    valid_fields = ['client', 'items', 'status', 'payment']
    if field_name not in valid_fields:
        print(f"Ошибка: поле '{field_name}' недоступно для редактирования.")
        return False

    try:
        if field_name == 'client':
            current_record[field_name] = new_value
        elif field_name == 'items':
            if isinstance(new_value, list):
                current_record[field_name] = {item['name']: item.get('qty', 1) for item in new_value}
            else:
                print("Ошибка: поле 'items' должно быть списком словарей.")
                return False
        elif field_name == 'status':
            if new_value not in statuses:
                print(f"Ошибка: статус '{new_value}' не существует. Доступные: {statuses}")
                return False
            current_record[field_name] = new_value
        elif field_name == 'payment':
            try:
                current_record[field_name] = float(new_value)
            except ValueError:
                print("Ошибка: поле 'payment' должно быть числом.")
                return False
        
        history.append({
            "action": f"edit_{field_name}",
            "record_id": record_id,
            "old_value": current_record.get(field_name),
            "new_value": new_value,
            "timestamp": datetime.now().isoformat()
        })
        
        print(f"Запись {record_id} успешно обновлена.")
        return True
        
    except Exception as e:
        print(f"Произошла ошибка при редактировании: {e}")
        return False
