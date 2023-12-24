from core.drivers.driver_types.chrome_driver import ChromeDriver
from core.drivers.driver_types.firefox_driver import FirefoxDriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox


class DriverManager:
    driver: Chrome | Firefox = None

    @classmethod
    def init_driver(cls, browser, args):

        driver_mapping = {
            "chrome": ChromeDriver(),
            "firefox": FirefoxDriver(),
        }

        if cls.driver is None:
            cls.driver = driver_mapping[browser].create_driver(args)

        return cls.driver

    @classmethod
    def get_webdriver(cls):
        return cls.driver

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
