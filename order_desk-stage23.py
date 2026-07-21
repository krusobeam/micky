# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: OrderDesk
def print_table(headers, rows):
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > widths[i]:
                widths[i] = len(str(cell))
    lines = ['| ' + ' | '.join(str(h).ljust(widths[i]) for i, h in enumerate(headers)) + ' |']
    sep = '| ' + ' -+- '.join('-' * w for w in widths) + ' |'
    lines.append(sep)
    for row in rows:
        cells = [str(c) for c in row]
        lines.append('| ' + ' | '.join(cells[i].ljust(widths[i]) for i in range(len(headers))) + ' |')
    print('\n'.join(lines))
