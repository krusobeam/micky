# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: OrderDesk
def validate_date(date_str):
    """Проверяет корректность даты в формате ДД.ММ.ГГГГ."""
    try:
        parts = date_str.split('.')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            return False, "Дата должна быть в формате ДД.ММ.ГГГГ"
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= day <= 31 and 1 <= month <= 12):
            return False, "Неверный день или месяц в дате"
        if year < 2000 or year > 2100:
            return False, "Год выходит за допустимые пределы (2000-2100)"
        import calendar as cal
        max_day = cal.monthrange(year, month)[1]
        if day > max_day:
            return False, f"День {day} не существует для месяца {month}"
        return True, ""
    except Exception:
        return False, "Ошибка при проверке даты"
