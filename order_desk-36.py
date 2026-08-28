# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: OrderDesk
def repair_data():
    if not customers: return
    if not orders: return
    for order in orders:
        if order.get('status') not in STATUS_LIST:
            order['status'] = STATUS_LIST[0]
            log_event(order['id'], 'status', STATUS_LIST[0], 'Repair: invalid status')
        if order.get('total') != sum(p['price'] * p['qty'] for p in order.get('items', [])):
            order['total'] = sum(p['price'] * p['qty'] for p in order.get('items', []))
            log_event(order['id'], 'total', order['total'], 'Repair: recalc total')
    for customer in customers:
        if not customer.get('orders') or not isinstance(customer['orders'], list):
            customer['orders'] = []
            log_event(customer['id'], 'orders', customer['orders'], 'Repair: missing orders list')
