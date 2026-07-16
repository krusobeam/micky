# === Stage 20: Добавь восстановление записей из архива ===
# Project: OrderDesk
def restore_archive_records():
    """Восстанавливает записи из архива в активные таблицы."""
    archive_path = "orderdesk_archive.json"
    if not os.path.exists(archive_path):
        print("Архив не найден.")
        return
    with open(archive_path, 'r', encoding='utf-8') as f:
        records = json.load(f)
    for record in records:
        table_name = record.pop('_table')
        if table_name not in DATA_TABLES:
            print(f"Таблица {table_name} не найдена в текущей базе.")
            continue
        existing_ids = [r['id'] for r in DATA_TABLES[table_name]]
        if record.get('id') and record['id'] in existing_ids:
            print(f"Запись с id={record['id']} уже существует, пропуск.")
            continue
        DATA_TABLES[table_name].append(record)
    print(f"Восстановлено {len(records)} записей из архива.")

restore_archive_records()
