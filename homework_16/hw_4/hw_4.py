def print_escape_table(escape_element: str, name: str) -> str:
    if 11 < len(name) < 20:
        tab_number = 3
    elif len(name) < 10 or len(name) == 11:
        tab_number = 4
    elif len(name) > 20:
        tab_number = 1
    else:
        tab_number = 0
    return f'|\t{escape_element}\t|\t{name}' + '\t' * tab_number + '|'
