from passenger import Passenger
from train import Train
from train_car import TrainCar

if __name__ == "__main__":
    # E.g.
    passenger1 = Passenger('John Down', 'Berlin', 9)
    passenger2 = Passenger('John Blob', 'Berlin', 10)
    passenger3 = Passenger('John Track', 'Berlin', 11)
    passenger4 = Passenger('John Fill', 'Berlin', 12)
    passenger5 = Passenger('John Stuart', 'Berlin', 13)
    railway_car1 = TrainCar('04589091', 50, [passenger1, passenger2, passenger3, passenger4, passenger5])
    print(len(railway_car1))
    print(passenger1)
    print(railway_car1)
    railway_car2 = TrainCar('04589045', 50, [passenger1, passenger2, passenger3, passenger4, passenger5])
    train1 = Train(20, [railway_car1, railway_car2])
    print(len(train1))
    print(train1)
