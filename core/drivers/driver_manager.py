from core.drivers.driver_types.chrome_driver import ChromeDriver
from core.drivers.driver_types.firefox_driver import FirefoxDriver


class DriverManager:
    driver = None

    @classmethod
    def init_driver(cls, browser):

        driver_mapping = {
            "chrome": ChromeDriver(),
            "firefox": FirefoxDriver(),
        }

        if cls.driver is None:
            cls.driver = driver_mapping[browser].create_driver()

        return cls.driver

    @classmethod
    def get_webdriver(cls):
        return cls.driver

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
