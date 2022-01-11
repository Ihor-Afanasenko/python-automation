from singleton import Singleton


class Printer(Singleton):
    """
    Printer inherited class Singleton and implementing singleton pattern
    """
    def new_print(self, number_page: int) -> str:
        return f'Print {number_page}.'


if __name__ == '__main__':
    # E.g.
    print1 = Printer()
    print2 = Printer()
    print(print1.new_print(10))
    print(print2.new_print(30))
    print(f'{print1} == {print2}')
    print(id(print1) == id(print2))
