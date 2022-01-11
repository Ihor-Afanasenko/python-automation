from passenger import Passenger


class TrainCar:
    """
    Describes general train car with number -> string (consist of 9 number, start with 0), number place
    and list passenger. Has method to add passenger or group of passenger as a list
    """

    def __init__(self, car_number: str, number_place: int, passengers: list[Passenger]) -> None:
        self.__car_number = car_number
        self.__number_place = number_place
        if self.__number_place >= len(passengers):
            self.__passengers = passengers
        else:
            raise Exception(f'This railway car full. You can not add more {self.__number_place} passengers')

    def __len__(self) -> int:
        return len(self.__passengers)

    def __str__(self) -> str:
        result = ''
        for car in self.__passengers:
            result += repr(car)+',\n'
        result = result[:-2]
        return f'[\n{result}\n]'

    def __repr__(self) -> str:
        return f'[{self.__car_number}]'

    @property
    def car_number(self) -> str:
        return self.__car_number

    @property
    def number_place(self) -> int:
        return self.__number_place

    def add_passenger(self, passenger: Passenger) -> list[Passenger]:
        if len(self.__passengers) <= self.__number_place:
            self.__passengers.append(passenger)
        else:
            raise Exception('This railway car full. You can not add new passenger')
        return self.__passengers

    def add_passengers(self, passengers: list[Passenger]) -> list[Passenger]:
        if len(self.__passengers) + len(passengers) <= self.__number_place:
            self.__passengers.extend(passengers)
        else:
            raise Exception('This railway car full. You can not add new group of passengers')
        return self.__passengers
