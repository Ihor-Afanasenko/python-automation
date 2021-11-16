def print_escape_table(escape_element, name):
    if 11 < len(name) < 20:
        tab_number = 3
    elif len(name) < 10 or len(name) == 11:
        tab_number = 4
    elif len(name) > 20:
        tab_number = 1
    else:
        tab_number = 0
    print(f'|\t{escape_element}\t|\t{name}' + '\t' * tab_number + '|')


print('Escape sequences table:')
print('-' * 37)
print_escape_table(r'\a', 'Bell (alert)')
print_escape_table(r'\b', 'Backspace')
print_escape_table(r'\n', 'New line')
print_escape_table(r'\t', 'Horizontal tab')
print_escape_table(r'\\', 'Backslash \\')
print_escape_table(r'\"', 'Double quotation mark \"')
print_escape_table(r'\'', 'Single quotation mark \'')
print('-' * 37)
