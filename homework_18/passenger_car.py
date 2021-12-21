from railway_car import RailwayCar
from car_state import CarState


class PassengerCar(RailwayCar):
    def __init__(self,
                 car_id: str,
                 tara: int,
                 average_speed: int,
                 number_axles: int,
                 car_type: str,
                 state: CarState,
                 owner: str,
                 passenger_number: int) -> None:
        super().__init__(car_id, tara, average_speed, number_axles, car_type, state, owner)
        self.__passenger_number = passenger_number

    def calculate_mass_gross(self) -> float:
        return self.tara + self.__passenger_number*0.1*9.81

    def calculate_coefficient_technic_efficient(self) -> float:
        return self.__passenger_number / self.tara
