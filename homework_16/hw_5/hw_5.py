def task_one(first_str: str = "john marta james Morgan Adam Maria huang") -> str:
    str_list = first_str.split(' ')
    new_list = []
    for element in str_list:
        new_list.append(element.capitalize())
    return ' '.join(new_list)


def task_two(list_str: tuple = ("John", "Marta", "James", "Amanda", "Marianna")) -> list:
    result = ['Names'.center(15, '*')]
    for element in list_str:
        result.append(f'{element : >15}')
    return result


def task_three(input_str: str = " name=Amanda=sssss&age=32&&salary=1500&currency=quro ") -> str:
    input_str = input_str.strip()
    result = []
    input_str = input_str.replace('&&', '&')
    input_str = input_str.split('&')
    for element in input_str:
        if '&' in element:
            element = element.replace('&', '')
        elif '=sssss' in element:
            element = element.replace('=sssss', '?sssss')
        element = element.replace('=', ': ')
        if '?' in element:
            element = element.replace('?', '=')
        result.append(element)
    return '{' + ', '.join(result) + '}'


def task_three_another_variant(input_str: str = " name=Amanda=sssss&age=32&&salary=1500&currency=quro ") -> dict:
    first_str = input_str.strip()
    result = []
    first_str = first_str.replace('&&', '&')
    list_str = first_str.split('&')
    for element in list_str:
        if '&' in element:
            element = element.replace('&', '')
        elif '=sssss' in element:
            element = element.replace('=sssss', '?sssss')
        element = element.split('=')
        result += element
    fix_result = []
    for element in result:
        if '?' in element:
            element = element.replace('?', '=')
        fix_result.append(element)
    return dict(zip(fix_result[::2], fix_result[1::2]))


def task_four(list_str: tuple = ("FirstItem", "FriendsList", "MyTuple")) -> list:
    result = []
    for element in list_str:
        new_element = []
        for char in element:
            if char.isupper() and element.index(char) != 0:
                char = char.replace(char, '_' + char.lower())
            new_element.append(char)
        new_str = ''.join(new_element)
        result.append(new_str.lower())
    return result


def task_five(data_input: str) -> list:
    result = []
    # split string for '. '
    for statement in data_input.strip().split('\n'):
        result += statement.strip().split('. ')
    # add '.' and update '..'
    final_result = []
    for element in result:
        element = element + '.'
        if '..' in element:
            element = element.replace('..', '.')
        final_result.append(element)
    return final_result


if __name__ == "__main__":
    # E.g.
    print(task_one())
    print(task_two())
    print(task_three())
    print(task_three_another_variant())
    print(task_four())

    data = """
    Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
    Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
    Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}
    У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
    У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше.
    """
    print(task_five(data))
