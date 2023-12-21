from core.utils.element import Element
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BooksPage(BasePage):

    def __init__(self):
        super().__init__()
        self.search_input = Element((By.XPATH, "//*[@id='searchBox']"))

    def fill_search_input(self, data):
        self.search_input.enter_text(data)
