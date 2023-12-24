from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from core.drivers.driver_types.base_driver import BaseDriver


class ChromeDriver(BaseDriver):

    def create_driver(self, args):
        options = webdriver.ChromeOptions()

        if args:
            for arg in args.split(","):
                options.add_argument(f"--{arg}")

        return webdriver.Chrome(service=ChromeService(), options=options)
