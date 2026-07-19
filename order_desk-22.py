# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: OrderDesk
def check_overdue_reminders():
    overdue = []
    now = datetime.now()
    for order in orders:
        if order.reminder_date and order.status != 'completed' and order.reminder_date < now:
            overdue.append((order, (now - order.reminder_date).days))
    return overdue

def send_overdue_notifications():
    overdue = check_overdue_reminders()
    for order, days in overdue:
        print(f"Просроченное напоминание: заказ #{order.id}, клиент {order.client_name}, пропущено дней: {days}")
