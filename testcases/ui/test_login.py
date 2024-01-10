import pytest
import allure
from core.report.allure_report import Report
from models.account import Account
from pages.home_page import HomePage


@allure.parent_suite('Demo Test')
@allure.suite('Test login')
class TestLogin:

    @allure.title("Login with valid account")
    @pytest.mark.smoke
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('./resources/test_data/accounts.json', 'valid'))
    def test_search_login_valid(self, account: Account):
        
        home_page = HomePage()
        login_page = home_page.click_login_btn();
        login_page.fill_login_information(account.username, account.password)
        login_page.submit_login()
        
        is_username_lbl_displayed = home_page.is_username_lbl_displayed()
        expected_username = home_page.get_username_lbl_value()
        
        assert is_username_lbl_displayed is True, "Username label should displayed"
        assert expected_username == account.username, f"Username should be {account.username}"
        