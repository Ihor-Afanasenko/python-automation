data = """
Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}
У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше.
"""

print('Exercise 1')
first_str = "john marta james Morgan Adam Maria huang"
str_list = first_str.split(' ')
new_list = []
for element in str_list:
    new_list.append(element.capitalize())
print(' '.join(new_list))

print('\nExercise 2')
list_str = ["John", "Marta", "James", "Amanda", "Marianna"]
print('Names'.center(15, '*'))
for element in list_str:
    print(f'{element : >15}')

print('\nExercise 3')
first_str = " name=Amanda=sssss&age=32&&salary=1500&currency=quro "
first_str = first_str.strip()
result = []
first_str = first_str.replace('&&', '&')
list_str = first_str.split('&')
for element in list_str:
    if '&' in element:
        element = element.replace('&', '')
    elif '=sssss' in element:
        element = element.replace('=sssss', '?sssss')
    element = element.replace('=', ': ')
    if '?' in element:
        element = element.replace('?', '=')
    result.append(element)
result = '{' + ', '.join(result) + '}'
print(result)

# or
print('\nExercise 3b')
first_str = " name=Amanda=sssss&age=32&&salary=1500&currency=quro "
first_str = first_str.strip()
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
result_dict = dict(zip(fix_result[::2], fix_result[1::2]))
print(result_dict)

print('\nExercise 4')
str_list = ["FirstItem", "FriendsList", "MyTuple"]
result = []
for element in str_list:
    new_element = []
    for char in element:
        if char.isupper() and element.index(char) != 0:
            char = char.replace(char, '_' + char.lower())
        new_element.append(char)
    new_str = ''.join(new_element)
    result.append(new_str.lower())
print(result)

print('\nExercise 5')
# split string for paragraph
data = data.strip().split('\n')
result = []
# split string for '. '
for statement in data:
    result += statement.split('. ')
# add '.' and update '..'
for element in result:
    element = element + '.'
    if '..' in element:
        element = element.replace('..', '.')
    print(element)
