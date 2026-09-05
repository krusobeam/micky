# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: OrderDesk
def dry_run(operation, args, dry_mode=False):
    """Execute operation in dry-run mode if enabled, else run normally."""
    if dry_mode:
        print(f"[DRY-RUN] {operation} with args: {args}")
        return None
    return operation(args)
