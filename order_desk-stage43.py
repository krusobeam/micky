# === Stage 43: Добавь пагинацию длинных списков ===
# Project: OrderDesk
def paginate(items, page=1, page_size=20):
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "total": len(items),
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }
