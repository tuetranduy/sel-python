from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from core.drivers.driver_types.base_driver import BaseDriver


class FirefoxDriver(BaseDriver):

    def create_driver(self, args):
        options = webdriver.FirefoxOptions()
        
        if args:
            for arg in args.split(","):
                options.add_argument(f"--{arg}")
        
        return webdriver.Firefox(service=FirefoxService(), options=options)