import pytest

from core.drivers.driver_manager import DriverManager

@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    DriverManager.init_driver()
    DriverManager.get_webdriver().maximize_window()
    DriverManager.get_webdriver().get("https://demoqa.com/books")

    yield
    DriverManager.quit_driver()
