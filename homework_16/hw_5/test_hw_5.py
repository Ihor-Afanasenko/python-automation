import unittest
import hw_5


class TestHomework5(unittest.TestCase):

    def test_task_one_upper_element(self):
        """ Check output result every word start with uppercase """
        out = hw_5.task_one()
        for element in out.split(' '):
            self.assertEqual(element[0], element[0].upper())

    def test_task_one_result_is_string(self):
        """ Check output result is string """
        self.assertIsInstance(hw_5.task_one(), str)

    def test_task_one_return_number_word(self):
        """ Check output result return number of word """
        out = hw_5.task_one("john marta james Morgan Adam Maria huang")
        self.assertEqual(len(out.split(' ')), 7)

    def test_task_two_has_header(self):
        """ Check output result has header """
        out = hw_5.task_two()
        self.assertEqual(out[0], '*****Names*****')

    def test_task_two_has_elements(self):
        """ Check output result has elements """
        check_data = ("John", "Marta", "James", "Amanda", "Marianna")
        out = hw_5.task_two(check_data)
        for i in range(len(check_data)):
            self.assertIn(check_data[i], out[i + 1])

    def test_task_two_return_list(self):
        """ Check output result is list """
        self.assertIsInstance(hw_5.task_two(), list)

    def test_task_three_equal(self):
        """ Check output result return format string """
        self.assertEqual(hw_5.task_three(" name=Amanda=sssss&age=32&&salary=1500&currency=quro "),
                         '{name: Amanda=sssss, age: 32, salary: 1500, currency: quro}')

    def test_task_three_return_string(self):
        """ Check output result return string """
        self.assertIsInstance(hw_5.task_three(), str)

    def test_task_three_return_elements(self):
        """ Check output result return elements """
        out = hw_5.task_three(" name=Amanda=sssss&age=32&&salary=1500&currency=quro ")
        out_elements = []
        for element in out.split(', '):
            out_elements += element.split(': ')
        check_data = ("name", "Amanda=sssss", "age", "32", "salary", "1500", "currency", "quro")
        for i in range(len(check_data)):
            self.assertIn(check_data[i], out_elements[i])

    def test_three_another_variant_keys(self):
        """ Check output result return correct keys """
        out = hw_5.task_three_another_variant(" name=Amanda=sssss&age=32&&salary=1500&currency=quro ")
        check_keys = ('name', 'age', 'salary', 'currency')
        i = 0
        for key in out.keys():
            self.assertEqual(key, check_keys[i])
            i += 1

    def test_three_another_variant_values(self):
        """ Check output result return correct values """
        out = hw_5.task_three_another_variant(" name=Amanda=sssss&age=32&&salary=1500&currency=quro ")
        check_values = ('Amanda=sssss', '32', '1500', 'quro')
        i = 0
        for value in out.values():
            self.assertEqual(value, check_values[i])
            i += 1

    def test_three_another_variant_result_is_dict(self):
        """ Check output result is dict """
        self.assertIsInstance(hw_5.task_three_another_variant(), dict)

    def test_task_four_equal_elements(self):
        """ Check output result return elements """
        out = hw_5.task_four(("FirstItem", "FriendsList", "MyTuple"))
        check_data = ("first_item", "friends_list", "my_tuple")
        for i in range(len(check_data)):
            self.assertIn(check_data[i], out[i])

    def test_task_four_result_is_list(self):
        """ Check output result is list """
        self.assertIsInstance(hw_5.task_four(), list)

    def test_task_four_all_elements_downcase(self):
        """ Check output result return elements in downcase """
        out = hw_5.task_four(("FirstItem", "FriendsList", "MyTuple"))
        for string in out:
            for char in string:
                self.assertEqual(char, char.lower())

    def test_task_four_string_has_character(self):
        """ Check output result has character _ """
        out = hw_5.task_four(("FirstItem", "FriendsList", "MyTuple"))
        for string in out:
            self.assertIn('_', string)

    def test_task_five_all_elements_start_uppercase(self):
        """ Check output result has elements start with uppercase """
        data = """
            Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
            Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
            Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}
            У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
            У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше.
            """
        out = hw_5.task_five(data)
        for sentence in out:
            self.assertEqual(sentence[0], sentence[0].upper())

    def test_task_five_all_elements_finish_dot(self):
        """ Check output result has elements finish dot """
        data = """
            Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
            Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
            Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}
            У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
            У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше.
            """
        out = hw_5.task_five(data)
        for sentence in out:
            self.assertEqual(sentence[-1], '.')

    def test_task_five_result_is_list(self):
        """ Check output result is list """
        data = """
            Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
            Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
            Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}
            У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
            У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше.
            """
        self.assertIsInstance(hw_5.task_five(data), list)

    def test_task_five_types(self):
        """ Check output result has not incorrect type """
        data = """
            Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
            Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
            Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}
            У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
            У вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений. Текст -все чтот выше.
            """
        for check_type in (int, float, str, tuple, set, dict):
            self.assertNotIsInstance(hw_5.task_five(data), check_type, f"Output has type {type(check_type)}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
