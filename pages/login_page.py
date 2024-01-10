from core.utils.element import Element
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.username_input = Element((By.ID, "userName"))
        self.password_input = Element((By.ID, "password"))

    def fill_login_information(self, username, password):
        self.username_input.enter_text(username)
        self.password_input.enter_text(password)

    def submit_login(self):
        self.login_btn.click()
