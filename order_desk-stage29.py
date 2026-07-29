# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: OrderDesk
def get_app_config():
    config = {
        "app_name": "OrderDesk",
        "version": "29",
        "default_status": "new",
        "statuses": ["new", "confirmed", "processing", "shipped", "delivered", "cancelled"],
        "payment_methods": ["cash", "card", "wallet"],
        "max_order_items": 10,
        "log_history_limit": 50,
    }
    return config


def save_app_config(config_path="app_config.json"):
    import json

    with open(config_path, "w") as f:
        json.dump(get_app_config(), f, indent=2)


def load_app_config(config_path="app_config.json"):
    import json

    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        save_app_config()
        return get_app_config()


def update_config(key, value):
    config = load_app_config()
    if key in config:
        config[key] = value
        save_app_config()
        return True
    else:
        raise KeyError(f"Unknown config key: {key}")


if __name__ == "__main__":
    print("Config:", get_app_config())
