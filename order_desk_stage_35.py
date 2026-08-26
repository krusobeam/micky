# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: OrderDesk
def next_action_suggestion(current_state, actions_log):
    if not current_state:
        return "Система пуста. Начните с создания клиента."
    last_action = actions_log[-1] if actions_log else None
    if last_action["type"] == "create_order":
        return "Добавьте позицию в заказ или измените его статус."
    if last_action["type"] == "add_position":
        return "Измените количество или цену позиции."
    if last_action["type"] == "change_status":
        return "Обновите статус заказа на 'completed' или 'cancelled'."
    if last_action["type"] == "add_payment":
        return "Попробуйте отменить заказ или создать новый."
    return "Система работает корректно. Добавьте следующий элемент."
