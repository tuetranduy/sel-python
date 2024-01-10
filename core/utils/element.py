from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC
from core.drivers.driver_manager import DriverManager
from selenium.webdriver.common.by import By

from core.utils.wait_utils import WaitUtils


class Element:

    def __init__(self, locator: Tuple[By, str]):
        self._element = None
        self._locator = locator
        self._driver = DriverManager.get_webdriver()

    def wait_element_to_be_visible(self):
        wait = WaitUtils(self._driver)
        self._element = wait.web_driver_wait_default().until(
            EC.visibility_of_element_located((self._locator[0], self._locator[1])))

    def enter_text(self, text):
        self.wait_element_to_be_visible()
        self._element.clear()
        self._element.send_keys(text)

    def click(self):
        self.wait_element_to_be_visible()
        self._element.click()

    def is_element_displayed(self):
        try:
            self.wait_element_to_be_visible()
            return True
        except:
            return False

    def get_inner_html(self):
        self.wait_element_to_be_visible()
        return self._element.get_attribute("innerHTML").strip()