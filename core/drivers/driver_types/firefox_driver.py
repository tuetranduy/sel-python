from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from core.drivers.driver_types.base_driver import BaseDriver


class FirefoxDriver(BaseDriver):

    def create_driver(self):
        options = webdriver.FirefoxOptions()
        
        return webdriver.Firefox(service=FirefoxService(), options=options)