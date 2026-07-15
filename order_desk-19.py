# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: OrderDesk
def archive_old_records(db, max_age_days=365):
    """Archive records older than max_age_days days."""
    import datetime
    
    cutoff = datetime.datetime.now() - datetime.timedelta(days=max_age_days)
    
    # Get all records with 'complete' or 'cancelled' status
    status_list = ['complete', 'cancelled']
    
    archived_count = 0
    for record in db.records:
        if record['status'] in status_list and record['created_at'] < cutoff:
            record['archived'] = True
            archived_count += 1
    
    return archived_count

# Add to existing database initialization
if not hasattr(database, 'records'):
    database.records = []

# Periodic archiving on startup
archive_old_records(database)
