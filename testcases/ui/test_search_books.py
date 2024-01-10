import pytest
import allure
from core.report.allure_report import Report
from models.book import Book

from pages.books_page import BooksPage


@allure.parent_suite('Demo Test')
@allure.suite('Test search Book with parameterize')
class TestSearchBook:

    @allure.title("Search valid book")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/book_search.json', 'valid'))
    def test_search_book_valid(self, book):

        books_page = BooksPage()

        Report.report_step(f"Search book with valid name: {book.book_name}")

        books_page.fill_search_input(book.book_name)

    @allure.title("Search invalid book")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/book_search.json', 'invalid'))
    def test_search_book_invalid(self, book):

        books_page = BooksPage()

        Report.report_step(f"Search book with invalid name: {book.book_name}")

        books_page.fill_search_input(book.book_name)
