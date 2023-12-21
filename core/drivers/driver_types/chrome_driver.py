from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from core.drivers.driver_types.base_driver import BaseDriver


class ChromeDriver(BaseDriver):

    def create_driver(self):
        options = webdriver.ChromeOptions()

        return webdriver.Chrome(service=Service(), options=options)
