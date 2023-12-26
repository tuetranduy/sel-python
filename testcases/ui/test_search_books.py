import pytest
import allure

from pages.books_page import BooksPage


@allure.parent_suite('Demo Test')
@allure.suite('Test search Book with parameterize')
class TestSearchBook:

    @allure.title("Search book")
    @pytest.mark.smoke
    @pytest.mark.parametrize("search_string", Book.get_list_book_from_json('resources/test_data/book_search.json','valid'))
    def test_search_book(self, search_string):

        books_page = BooksPage()

        books_page.fill_search_input("test 123")
