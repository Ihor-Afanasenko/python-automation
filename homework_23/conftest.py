import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def driver(scope='session'):
    driver = Chrome('./driver/chromedriver')
    driver.get("https://test.io/")
    driver.maximize_window()
    yield driver
    driver.quit()
