# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: OrderDesk
class OrderSearcher:
    def __init__(self, orders):
        self.orders = orders
    
    def search(self, **filters):
        if not filters:
            return list(self.orders)
        
        results = []
        for order in self.orders:
            match = True
            for key, value in filters.items():
                if key == 'status':
                    status_list = [s.strip().lower() for s in value] if isinstance(value, str) else value
                    if not any(order.status.lower() in s or s in order.status.lower() for s in status_list):
                        match = False
                        break
                elif key == 'client_name':
                    client_lower = order.client.name.lower().strip()
                    search_str = (value if isinstance(value, str) else value[0]).lower().strip()
                    if search_str and search_str not in client_lower:
                        match = False
                        break
                elif key == 'item_name':
                    item_list = [i.strip().lower() for i in order.items] if isinstance(order.items, list) else []
                    search_str = (value if isinstance(value, str) else value[0]).lower().strip()
                    if search_str and not any(search_str in item for item in item_list):
                        match = False
                        break
                elif key == 'payment_status':
                    payment_lower = order.payment.status.lower().strip() if order.payment else ''
                    status_list = [s.strip().lower() for s in value] if isinstance(value, str) else value
                    if not any(payment_lower in s or s in payment_lower for s in status_list):
                        match = False
                        break
            
            if match:
                results.append(order)
        
        return results
