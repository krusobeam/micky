# === Stage 17: Добавь группировку записей по категориям ===
# Project: OrderDesk
def group_records(records, key_func):
    grouped = {}
    for record in records:
        key = key_func(record)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(record)
    return dict(sorted(grouped.items()))
