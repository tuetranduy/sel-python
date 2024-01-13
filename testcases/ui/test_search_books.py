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
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/books.json', 'valid'))
    def test_search_book_valid(self, book: Book):
        Report.report_step(f"Search book with valid name: {book.book_name}")

        books_page = BooksPage()
        books_page.fill_search_input(book.book_name)
        is_book_displayed = books_page.is_book_displayed_correctly(book.book_name)
        
        assert is_book_displayed is True

    @allure.title("Search invalid book")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/books.json', 'invalid'))
    def test_search_book_invalid(self, book):

        Report.report_step(f"Search book with invalid name: {book.book_name}")

        books_page = BooksPage()
        books_page.fill_search_input(book.book_name)
        
        is_no_rows_found_lbl_displayed = books_page.is_no_rows_found_lbl_displayed()
        
        assert is_no_rows_found_lbl_displayed is True
