# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: OrderDesk
import shutil, os, datetime

def backup_data_file(data_path, backup_dir=None):
    if not os.path.exists(data_path):
        return None
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_path), 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    bak = os.path.join(backup_dir, f'backup_{ts}.json')
    shutil.copy2(data_path, bak)
    return bak

backup_data_file('orders.json')
