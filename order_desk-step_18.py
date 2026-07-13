# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: OrderDesk
def add_tag(order_id, tag):
    try:
        order = find_order(order_id)
        if not order['tags']:
            order['tags'] = []
        for t in order['tags']:
            if t == tag:
                return order
        order.setdefault('tags', []).append(tag)
        return order
    except (KeyError, TypeError):
        raise ValueError(f"Order {order_id} not found")

def remove_tag(order_id, tag):
    try:
        order = find_order(order_id)
        if not order['tags']:
            return order
        new_tags = [t for t in order['tags'] if t != tag]
        if len(new_tags) == len(order['tags']):
            return order
        order['tags'] = new_tags
        history.append({"action": "remove_tag", "order_id": order_id, "tag": tag})
        return order
    except (KeyError, TypeError):
        raise ValueError(f"Order {order_id} not found")
