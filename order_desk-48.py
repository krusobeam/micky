# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: OrderDesk
class OrderStatus:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"OrderStatus({self.name!r}, {self.code!r})"
