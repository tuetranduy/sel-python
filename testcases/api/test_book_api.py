import pytest
import allure
from pytest_schema import schema
from apis.book_apis import BookAPIs
from core.report.allure_report import Report
from models.book import Book
from resources.test_data.api_schemas.book_schemas import BookSchemas


@allure.parent_suite('Demo API test')
@allure.suite('Test book APIs')
class TestBookAPI:

    @allure.title("Get book api")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/books.json', 'valid'))
    def test_get_book_api(self, get_access_token, book: Book):
        Report.report_step(f"Get book with isbn: {book.isbn}")

        response = BookAPIs.get_book(get_access_token, book.isbn)

        actual_isbn = response.get("isbn")
        actual_title = response.get("title")

        assert actual_isbn == book.isbn
        assert actual_title == book.book_name
        assert schema(BookSchemas.book_schema) == response
