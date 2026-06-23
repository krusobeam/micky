# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: OrderDesk
def filter_orders(status=None, category=None, tags=None):
    filtered = []
    for order in orders:
        if status and order['status'] != status: continue
        if category and order.get('category') != category: continue
        if tags is not None:
            order_tags = set(order.get('tags', []))
            if not any(t in order_tags for t in tags): continue
        filtered.append(order)
    return filtered
