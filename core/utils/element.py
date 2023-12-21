from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC
from core.drivers.driver_manager import DriverManager
from selenium.webdriver.common.by import By

from core.utils.wait_utils import WaitUtils


class Element:

    def __init__(self, locator: Tuple[By, str]):
        self._element = None
        self._locator = locator
        self._driver = DriverManager.init_driver()

    def element_to_be_visible(self):
        wait = WaitUtils(self._driver)
        self._element = wait.web_driver_wait_default().until(
            EC.visibility_of_element_located((self._locator[0], self._locator[1])))

    def enter_text(self, text):
        self.element_to_be_visible()
        self._element.clear()
        self._element.send_keys(text)

    def click(self, locator):
        self.element_to_be_visible(locator)
        self._element.click()
