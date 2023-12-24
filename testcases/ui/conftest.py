import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.drivers.driver_manager import DriverManager
from core.utils.driver_utils import DriverUtils


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    DriverManager.init_driver(pytest.browser, pytest.args)
    DriverUtils.maximize_window()
    DriverUtils.open_url("https://demoqa.com/books")

    yield
    DriverManager.quit_driver()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if call.when == "call":
        if report.failed:
            screenshot_path = "/test-result/screenshot/" + \
                              datetime.date.today().strftime("%Y-%m-%d_%H%M") + ".png"
            DriverUtils.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path, attachment_type=AttachmentType.PNG)
