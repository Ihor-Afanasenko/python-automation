from railway_car import RailwayCar
from car_state import CarState


class FreightCar(RailwayCar):
    def __init__(self,
                 car_id: str,
                 tara: float,
                 average_speed: int,
                 number_axles: int,
                 car_type: str,
                 state: CarState,
                 owner: str,
                 carrying: int) -> None:
        super().__init__(car_id, tara, average_speed, number_axles, car_type, state, owner)
        self.__carrying = carrying

    def calculate_mass_gross(self) -> float:
        return self.tara + self.__carrying

    def calculate_coefficient_technic_efficient(self) -> float:
        return self.tara / self.__carrying
