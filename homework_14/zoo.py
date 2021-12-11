from typing import List
from animal import Animal
from director import Director
from zoo_employee import ZooEmployee
from cage import Cage


class Zoo:
    """
    Contains a list of Cage objects with Animals, director, list of Zoo employee.
    Return year zoo income and check overload employees.
    """

    def __init__(
            self,
            name: str,
            cage_list: List[Cage],
            director: Director,
            zoo_employee: List[ZooEmployee],
            annual_donations: int,
            year_number_visitor: int,
            admission_price: int
    ) -> None:
        self.__name = name
        self.__cage_list = cage_list
        self.__director = director
        self.__zoo_employee = zoo_employee
        self.__annual_donations = annual_donations
        self.__year_number_visitor = year_number_visitor
        self.__admission_price = admission_price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cage_list(self) -> List[Cage]:
        return self.__cage_list

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def zoo_employee(self) -> List[ZooEmployee]:
        return self.__zoo_employee

    @property
    def annual_donations(self) -> int:
        return self.__annual_donations

    @annual_donations.setter
    def annual_donations(self, annual_donations: int):
        self.__annual_donations = annual_donations

    @property
    def year_number_visitor(self) -> int:
        return self.__year_number_visitor

    @year_number_visitor.setter
    def year_number_visitor(self, year_number_visitor: int):
        self.__year_number_visitor = year_number_visitor

    @property
    def admission_price(self) -> int:
        return self.__admission_price

    @admission_price.setter
    def admission_price(self, admission_price: int):
        self.__admission_price = admission_price

    def calculate_year_income(self) -> int:
        year_employees_salary = sum([employee.calculate_year_salary() for employee in self.__zoo_employee])
        year_cages_cost = sum([cage.calculate_year_cage_cost() for cage in self.__cage_list])
        year_zoo_cost = year_cages_cost + self.__director.calculate_year_salary() + year_employees_salary
        return self.__year_number_visitor * self.__admission_price + self.__annual_donations - year_zoo_cost

    def check_overload_employee(self) -> str:
        year_employees_work_hour = sum([employee.calculate_work_hour_per_year() for employee in self.__zoo_employee])
        year_animals_need_service = sum([cage.calculate_year_cage_hour_service() for cage in self.__cage_list])
        number_result = year_employees_work_hour - year_animals_need_service
        if number_result < 0:
            result = f"Zoo needs not less {int(abs(number_result) / year_employees_work_hour)} employee(s), animals need {abs(number_result)} hours for service per year "
        elif number_result > 0:
            result = f"Zoo not needs employees, employees have {number_result} free hours in year"
        else:
            result = "Zoo not needs new employees"
        return result


if __name__ == "__main__":
    # E.g.
    director_John = Director("John Smith", 1500)
    lion_Leo = Animal("Leo", "lion", 40, 50000, 8)
    lion_Peter = Animal("Peter", "lion", 40, 50000, 10)
    wolf = Animal("Mark", "wolf", 20, 5000, 9)
    zoo_keeper_Brad = ZooEmployee("Brad", "zookeeper", 800, 40)
    zoo_keeper_Phil = ZooEmployee("Phil", "zookeeper", 900, 50)
    first_cage = Cage('First', [lion_Leo, lion_Peter], 60)
    second_cage = Cage('Second', [wolf], 25)
    mini_zoo = Zoo('Mini zoo', [first_cage, second_cage], director_John, [zoo_keeper_Phil, zoo_keeper_Brad], 1000000,
                   1000, 50)
    print(mini_zoo.calculate_year_income())
    print(mini_zoo.check_overload_employee())
    mini_zoo.year_number_visitor = 100
    mini_zoo.annual_donations = 10000
    print(mini_zoo.calculate_year_income())
    print(mini_zoo.check_overload_employee())
