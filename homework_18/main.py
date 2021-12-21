from car_state import CarState
from freight_car import FreightCar
from passenger_car import PassengerCar

if __name__ == '__main__':
    # E.g.
    open_car = FreightCar('69823423', 20, 90, 4, 'open_car', CarState.ON_WAY, 'X', 73)
    print(open_car.send_to_destination())
    print(open_car.calculate_mass_gross())
    print(open_car.calculate_axel_load())
    print(open_car.calculate_coefficient_technic_efficient())
    print(open_car.download())
    print(open_car.service())
    print(open_car)

    passenger_car = PassengerCar('04323423', 52, 100, 4, 'compartmental', CarState.READY_TO_SHIP, 'X', 54)
    print(passenger_car.send_to_destination())
    print(passenger_car.calculate_mass_gross())
    print(passenger_car.calculate_axel_load())
    print(passenger_car.calculate_coefficient_technic_efficient())
    print(passenger_car)
