from core.utils.element import Element
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BooksPage(BasePage):

    def __init__(self):
        super().__init__()
        self.search_input = Element((By.XPATH, "//*[@id='searchBox']"))
        self.no_rows_found_lbl = Element((By.CLASS_NAME, "rt-noData"))

    def fill_search_input(self, data):
        self.search_input.enter_text(data)

    def is_no_rows_found_lbl_displayed(self):
        return self.no_rows_found_lbl.is_element_displayed()

    def is_book_displayed_correctly(self, book_name):
        book_element = Element((By.ID, f"see-book-{book_name}"))
        return book_element.is_element_displayed()
