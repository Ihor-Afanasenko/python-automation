from datetime import date


class ZooEmployee:
    """
    Class describe Zoo Employee
    """

    def __init__(
            self,
            name: str,
            classification: str,
            month_salary: int,
            work_hour_per_week: int
    ) -> None:
        self.__name = name
        self.__classification = classification
        self.__month_salary = month_salary
        self.__work_hour_per_week = work_hour_per_week

    @property
    def name(self) -> str:
        return self.__name

    @property
    def classification(self) -> str:
        return self.__classification

    @property
    def month_salary(self) -> int:
        return self.__month_salary

    @property
    def work_hour_per_week(self) -> int:
        return self.__work_hour_per_week

    def calculate_year_salary(self) -> int:
        return 12 * self.__month_salary

    def calculate_work_hour_per_year(self) -> int:
        days_year = (date(date.today().year, 12, 31) - date(date.today().year, 1, 1)).days + 1
        weeks_year = days_year//7
        return weeks_year * self.__work_hour_per_week
