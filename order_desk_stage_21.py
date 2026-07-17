# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: OrderDesk
from datetime import date, timedelta

class Reminder:
    def __init__(self, reminder_type, target_id, due_date):
        self.reminder_type = reminder_type  # 'order', 'payment'
        self.target_id = target_id
        self.due_date = due_date

    def is_overdue(self):
        return date.today() > self.due_date

    @staticmethod
    def create_reminder(order, days_ahead=7):
        due = order['created'] + timedelta(days=days_ahead)
        return Reminder('order', order['id'], due)

    @staticmethod
    def create_payment_reminder(payment, days_ahead=30):
        due = payment['due_date'] + timedelta(days=days_ahead)
        return Reminder('payment', payment['id'], due)

def check_reminders(reminders_queue):
    overdue = []
    for r in reminders_queue:
        if r.is_overdue():
            overdue.append(r)
    return overdue
