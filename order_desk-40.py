# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: OrderDesk
import argparse

def main():
    parser = argparse.ArgumentParser(description='OrderDesk CLI')
    parser.add_argument('action', choices=['create_order', 'list_orders', 'show_order', 'pay_order', 'history'], help='Действие')
    parser.add_argument('--order-id', type=int, help='ID заказа')
    args = parser.parse_args()
    if args.action == 'create_order':
        print('Заказ создан')
    elif args.action == 'list_orders':
        print('Список заказов')
    elif args.action == 'show_order':
        print(f'Заказ #{args.order_id}')
    elif args.action == 'pay_order':
        print('Оплата')
    elif args.action == 'history':
        print('История')

main()
