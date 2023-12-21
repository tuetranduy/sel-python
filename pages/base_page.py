from selenium.webdriver.common.by import By

from core.utils.element import BaseElement


class BasePage(BaseElement):
    login_btn = (By.XPATH, "//a[@title='Login to your account']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click(self.login_btn)
