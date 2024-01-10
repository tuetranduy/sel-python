from selenium.webdriver.common.by import By

from core.utils.element import Element
from pages.base_page import BasePage
from pages.login_page import LoginPage


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.username_lbl = Element((By.ID, "userName-value"))
        
    def click_login_btn(self):
        self.login_btn.click()
        
        return LoginPage()

    def is_username_lbl_displayed(self):
        return self.username_lbl.is_element_displayed()

    def get_username_lbl_value(self):
        return self.username_lbl.get_inner_html()