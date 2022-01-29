class Passenger:
    """
    Describes passenger with parameters: name, destination to travel and place in train car
    """

    def __init__(self, name: str, destination: str, place: int) -> None:
        self.__name = name
        self.__destination = destination
        self.__place = place

    def __repr__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            key_without_class = str(key).split('__')[1]
            if type(value) is str:
                result += f'\"{key_without_class}\": \"{value}\''
            else:
                result += f'\"{key_without_class}\": {value}'
            if key_without_class not in 'place':
                result += ',\n'
        return '{\n'+f'{result}'+'\n}'
