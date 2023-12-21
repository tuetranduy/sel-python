import pytest

from pages.books_page import BooksPage


class TestLogin:

    @pytest.mark.smoke
    def test_search_book(self):
        
        books_page = BooksPage()
        
        books_page.fill_search_input("test 123")