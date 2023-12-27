import pytest
import allure
from models.Book import Book

from pages.books_page import BooksPage


@allure.parent_suite('Demo Test')
@allure.suite('Test search Book with parameterize')
class TestSearchBook:

    @allure.title("Search book")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('core/resources/test_data/book_search.json','invalid'))
    def test_search_book(self, book):

        books_page = BooksPage()

        books_page.fill_search_input(book.book_name)
