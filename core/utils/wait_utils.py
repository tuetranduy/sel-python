from selenium.webdriver.support.wait import WebDriverWait


class WaitUtils:

    def __init__(self, driver):
        self.driver = driver

    def web_driver_wait_default(self):
        return WebDriverWait(self.driver, 10)

    def web_driver_wait_custom(self, timeout):
        return WebDriverWait(self.driver, timeout)
