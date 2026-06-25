# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: OrderDesk
def sort_records(records, key='date', reverse=False):
    if not records: return []
    order_map = {'date': 0, 'priority': 1, 'name': 2}
    key_index = order_map.get(key.lower(), -1)
    if key_index == -1: raise ValueError(f"Unknown sort key: {key}")
    def get_sort_value(item):
        val = item.get('date') or item.get('priority', 0) or item.get('name', '')
        if isinstance(val, str): return (0, len(val), val.lower())
        if isinstance(val, int): return (1, val, '')
        return (2, 0, '')
    sorted_records = sorted(records, key=get_sort_value, reverse=reverse)
    for i in range(len(sorted_records)):
        item = sorted_records[i]
        date_val = item.get('date') or item.get('created_at', None)
        if isinstance(date_val, str):
            try:
                parsed_date = datetime.strptime(date_val[:10], '%Y-%m-%d')
                item['_sort_date'] = (parsed_date.year, parsed_date.month, parsed_date.day)
            except ValueError:
                continue
    return sorted_records
