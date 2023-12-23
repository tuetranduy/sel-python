from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from core.drivers.driver_types.base_driver import BaseDriver


class ChromeDriver(BaseDriver):

    def create_driver(self):
        options = webdriver.ChromeOptions()

        return webdriver.Chrome(service=ChromeService(), options=options)
