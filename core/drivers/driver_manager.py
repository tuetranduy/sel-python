from core.drivers.driver_types.chrome_driver import ChromeDriver


class DriverManager:
    driver = None

    @classmethod
    def init_driver(cls):
        if cls.driver is None:
            cls.driver = ChromeDriver().create_driver()

        return cls.driver

    @classmethod
    def get_webdriver(cls):
        return cls.driver

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
