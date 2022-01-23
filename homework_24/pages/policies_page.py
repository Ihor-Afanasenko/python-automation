from webbrowser import Chrome
from .base_page import BasePage


class PoliciesPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)

        self.__page_url = "https://test.io/policies"

    @property
    def page_url(self) -> str:
        return self.__page_url
