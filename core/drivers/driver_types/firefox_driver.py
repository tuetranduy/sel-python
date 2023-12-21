from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from core.drivers.driver_types.base_driver import BaseDriver


class FirefoxDriver(BaseDriver):

    def create_driver(self):
        options = webdriver.FirefoxOptions()
        self._driver = webdriver.Firefox(service=Service(), options=options)

        return self
