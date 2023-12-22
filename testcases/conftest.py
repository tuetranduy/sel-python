import pytest

from core.drivers.driver_manager import DriverManager
from core.utils.driver_utils import DriverUtils

@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    DriverManager.init_driver()
    DriverUtils.maximize_window()
    DriverUtils.open_url("https://demoqa.com/books")

    yield
    DriverManager.quit_driver()
