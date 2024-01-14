import pytest
import allure
from pytest_schema import schema
from apis.book_apis import BookAPIs
from core.report.allure_report import Report
from core.utils.constants import Constants
from models.book import Book
from resources.test_data.api_schemas.book_schemas import BookSchemas
from resources.test_data.api_schemas.common_schemas import CommonSchemas


@allure.parent_suite('Demo API test')
@allure.suite('Test book APIs')
class TestBookAPI:

    @allure.title("Get book with valid isbn api")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/books.json', 'valid'))
    def test_get_valid_book_api(self, get_access_token, book: Book):
        Report.report_step(f"Get book with valid isbn: {book.isbn}")

        response = BookAPIs.get_book(get_access_token, book.isbn)

        actual_status_code = response.get("status_code")
        actual_isbn = response.get("data").get("isbn")
        actual_title = response.get("data").get("title")

        assert schema(BookSchemas.book_success_response_schema) == response.get("data")
        assert actual_status_code == 200
        assert actual_isbn == book.isbn
        assert actual_title == book.book_name

    @allure.title("Get book with invalid isbn api")
    @pytest.mark.smoke
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('./resources/test_data/books.json', 'invalid'))
    def test_get_invalid_book_api(self, get_access_token, book: Book):
        Report.report_step(f"Get book with invalid isbn: {book.isbn}")

        response = BookAPIs.get_book(get_access_token, book.isbn)

        actual_status_code = response.get("status_code")
        actual_error_msg = response.get("data").get("message")

        assert schema(CommonSchemas.error_response_schema) == response.get("data")
        assert actual_status_code == 400
        assert actual_error_msg == Constants.INVALID_ISBN