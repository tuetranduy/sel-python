from core.utils.api_utils import ApiUtils


class BookAPIs:

    def get_book(access_token, isbn):
        api_utils = ApiUtils(access_token)
        response = api_utils.get(f"BookStore/v1/Book", {"ISBN": isbn})

        return response
