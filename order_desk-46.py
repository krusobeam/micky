# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: OrderDesk
DATA_VERSION = 46

def migrate_v46():
    """Добавляем поле is_active в статусы и историю."""
    if 'statuses' not in DATA:
        DATA['statuses'] = [
            {'id': 'new', 'label': 'Новый', 'is_active': True},
            {'id': 'processing', 'label': 'В обработке', 'is_active': True},
            {'id': 'completed', 'label': 'Завершён', 'is_active': True},
            {'id': 'cancelled', 'label': 'Отменён', 'is_active': False},
        ]
    if 'history' not in DATA:
        DATA['history'] = []
    for entry in DATA.get('history', []):
        if 'is_active' not in entry:
            entry['is_active'] = True
    return DATA
