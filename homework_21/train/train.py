from homework_21.train.train_car import TrainCar


class Train:
    """
    Describes general train with parameters: maximum train car then can locomotive move and list train cars.
    Has method to add train car or group of train cars as a list
    """

    def __init__(self, max_train_cars: int, train_cars: list[TrainCar]) -> None:
        self.__max_train_cars = max_train_cars
        if self.__max_train_cars >= len(train_cars):
            self.__train_cars = train_cars
        else:
            raise Exception(f'This train has max number {self.__max_train_cars} cars')

    def __len__(self) -> int:
        return len(self.__train_cars)

    def __str__(self) -> str:
        str_train_cars = ''
        for car in self.__train_cars:
            str_train_cars += f'-{repr(car)}'
        return f'[HEAD]{str_train_cars}'

    def add_train_car(self, train_car: TrainCar) -> list[TrainCar]:
        if len(self.__train_cars) <= self.__max_train_cars:
            self.__train_cars.append(train_car)
        else:
            raise Exception('Locomotive has max train cars. Change locomotive or add one more.')
        return self.__train_cars

    def add_train_cars(self, additional_train_cars: list[TrainCar]) -> list[TrainCar]:
        if len(self.__train_cars) + len(additional_train_cars) <= self.__max_train_cars:
            self.__train_cars.extend(additional_train_cars)
        else:
            raise Exception('Locomotive has max train cars. You can not add group of cars.')
        return self.__train_cars
