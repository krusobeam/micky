# === Stage 32: Добавь журнал действий пользователя ===
# Project: OrderDesk
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, details=None):
        entry = {
            'timestamp': datetime.now().isoformat(),
            'user': user,
            'type': action_type,
            'details': details or ''
        }
        self.entries.append(entry)
        return entry

    def get_recent(self, n=10):
        return list(reversed(self.entries[-n:]))


action_log = ActionLog()


def log_create_order(user, order_id):
    return action_log.log(user, 'create_order', f'Order {order_id} created')


def log_add_item(user, order_id, product_name, price):
    return action_log.log(user, 'add_item',
                           f'Added {product_name} to Order {order_id}: ${price}')


def log_cancel_order(user, order_id):
    return action_log.log(user, 'cancel_order', f'Order {order_id} cancelled')


def log_complete_payment(user, order_id, amount):
    return action_log.log(user, 'payment', f'Paid $amount for Order {order_id}')


def get_action_history(limit=10):
    return action_log.get_recent(limit)
