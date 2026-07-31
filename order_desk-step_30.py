# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: OrderDesk
def add_profile(name, role="user"):
    profiles[name] = {"name": name, "role": role}
    return profiles[name]
