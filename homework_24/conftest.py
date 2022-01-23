import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from .core.config import Config
from homework_24.pages import LandingPage


@pytest.fixture(scope="session")
def config() -> Config:
    yield Config()


@pytest.fixture(scope="session")
def driver(config) -> Chrome:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(config.driver_path, chrome_options=chrome_options)
    driver.get(config.host)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def landing_page(driver):
    yield LandingPage(driver)
