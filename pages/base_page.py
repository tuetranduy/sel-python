from core.utils.element import Element
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self):
        self.login_btn = Element((By.ID, "login"))
        pass
