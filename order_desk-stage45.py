# === Stage 45: Добавь восстановление из резервной копии ===
# Project: OrderDesk
import json, pathlib

BACKUP_PATH = pathlib.Path("orderdesk_backup.json")

def restore_backup():
    if not BACKUP_PATH.exists():
        print("Резервная копия не найдена.")
        return False
    try:
        with open(BACKUP_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("Неверный формат резервной копии.")
            return False
        db = {
            "clients": data.get("clients", []),
            "orders": data.get("orders", []),
            "payments": data.get("payments", []),
            "statuses": data.get("statuses", []),
            "history": data.get("history", []),
        }
        return db
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Ошибка чтения резервной копии: {e}")
        return False

def save_backup(db):
    with open(BACKUP_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print("Резервная копия сохранена.")
