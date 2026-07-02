# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: OrderDesk
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                add_record(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                add_record({**value, 'type': key})
        else:
            print("Ошибка: неверный формат JSON")
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке: {type(e).__name__}: {e}")
