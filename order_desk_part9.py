# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: OrderDesk
import json, sys, os

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        required_keys = ["clients", "items", "orders"]
        missing = [k for k in required_keys if k not in data]
        if missing:
            raise KeyError(f"Отсутствуют ключи: {', '.join(missing)}")
            
        # Валидация типов данных для основных сущностей
        if not isinstance(data["clients"], list) or \
           not all(isinstance(c, dict) and "id" in c for c in data["clients"]):
            raise ValueError("Некорректный формат 'clients'")
            
        if not isinstance(data["items"], list) or \
           not all(isinstance(i, dict) and "id" in i for i in data["items"]):
            raise ValueError("Некорректный формат 'items'")
            
        if not isinstance(data["orders"], list) or \
           not all(isinstance(o, dict) and "id" in o for o in data["orders"]):
            raise ValueError("Некорректный формат 'orders'")
            
        return {k: v for k, v in data.items()}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
# if __name__ == "__main__":
#     sample_data = '{"clients":[{"id":1,"name":"Alice"}],"items":[],"orders":[]}'
#     db_state = load_initial_data(sample_data)
