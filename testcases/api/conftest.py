import pytest

from core.utils.api_utils import ApiUtils


@pytest.fixture(scope="function", autouse=True)
def get_access_token():

    api_utils = ApiUtils()
    response = api_utils.post("Account/v1/GenerateToken", json={"userName": 'tuetest', "password": 'Password11!'})
    
    return response.get("data").get("token")