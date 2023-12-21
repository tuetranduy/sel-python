from selenium.webdriver.support import expected_conditions as EC

from core.utils.wait_utils import WaitUtils


class Element:

    def __init__(self, by):
        self._element = None
        self._by = by

    def element_to_be_visible(self, locator):
        return WaitUtils.web_driver_wait_default(self.driver).until(EC.visibility_of_element_located(locator))

    def enter_text(self, locator, text):
        element = self.element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.element_to_be_visible(locator)
        element.click()
