from abc import ABC, abstractmethod
from car_state import CarState


class RailwayCar(ABC):
    def __init__(self,
                 car_id: str,
                 tara: float,
                 average_speed: int,
                 number_axles: int,
                 car_type: str,
                 state: CarState,
                 owner: str
                 ) -> None:
        self.__car_id = car_id
        self.__tara = tara
        self.__average_speed = average_speed
        self.__number_axles = number_axles
        self.__car_type = car_type
        self.__state = state
        self.__owner = owner

    def __str__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            key_without_class = str(key).split('__')[1]
            result += f'{key_without_class} => {value}\n'
        return result

    @property
    def car_id(self) -> str:
        return self.__car_id

    @property
    def tara(self) -> float:
        return self.__tara

    @property
    def number_axles(self) -> int:
        return self.__number_axles

    @property
    def car_type(self) -> str:
        return self.__car_type

    @property
    def state(self) -> CarState:
        return self.__state.name

    @property
    def owner(self) -> str:
        return self.__owner

    @abstractmethod
    def calculate_mass_gross(self):
        """This method calculate general mass railway car"""
        ...

    def calculate_axel_load(self) -> float:
        """This method calculate force that load one car axel"""
        return self.calculate_mass_gross()*9.81/self.number_axles

    @abstractmethod
    def calculate_coefficient_technic_efficient(self):
        """This method calculating economic parameter railway car
        for freight car - tara division to carrying
        for passenger car - number of passenger division to tara"""
        ...

    def send_to_destination(self) -> str:
        if self.state == 'READY_TO_SHIP':
            return f'Car ready to ship. In state {self.state}'
        else:
            return f'Car not ready to ship. State {self.state}'

    def service(self) -> str:
        if self.state == 'SERVICE_NEEDED':
            return f'Car need service. Current state {self.state}'
        else:
            return f'Car not need service. Current state {self.state}'

    def repair(self) -> str:
        if self.state == 'REPAIR_REQUIRED':
            return f'Car require repair. Current state {self.state}'
        else:
            return f'Car not require repair. Current state {self.state}'

    def download(self) -> str:
        if self.state == 'LOADING':
            return f'Car in downloading. Current state {self.state}'
        elif self.state == 'REPAIR_REQUIRED' or self.state == 'SERVICE_NEEDED' or self.state == 'UNLOADING' or\
                self.state == 'ON_WAY':
            return f'Car can not downloading. Current state {self.state}'
        else:
            return f'Car can be downloading. Current state {self.state}'

    def unload(self) -> str:
        if self.state == 'UNLOADING':
            return f'Car in unloading. Current state {self.state}'
        elif self.state == 'REPAIR_REQUIRED' or self.state == 'SERVICE_NEEDED' or self.state == 'LOADING' or\
                self.state == 'ON_WAY':
            return f'Car can not unloading. Current state {self.state}'
        else:
            return f'Car can be unloading. Current state {self.state}'
