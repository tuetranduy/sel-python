from core.drivers.driver_manager import DriverManager


class DriverUtils:

    @classmethod
    def get_driver(cls):
        return DriverManager.get_webdriver()

    @classmethod
    def get_title(cls):
        return cls.get_driver().title

    @classmethod
    def maximize_window(cls):
        cls.get_driver().maximize_window()

    @classmethod
    def close_browser(cls):
        cls.get_driver().close()

    @classmethod
    def open_url(cls, url):
        cls.get_driver().get(url)

    @classmethod
    def select_main_window(cls):
        handles = cls.get_driver().window_handles
        cls.get_driver().switch_to.window(handles[0])

    @classmethod
    def accept_alert(cls):
        cls.wait_for_alert()
        alert = cls.get_driver().switch_to.alert
        alert.accept()

    @classmethod
    def save_screenshot(cls, file):
        cls.get_driver().save_screenshot(file)

    @classmethod
    def save_screenshot_as_png(cls):
        cls.get_driver().get_screenshot_as_png()
