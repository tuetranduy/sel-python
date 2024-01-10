import json
import os


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get_list_account_from_json(cls, json_file_path, account_type):
        result = []
        with open(os.path.abspath(json_file_path)) as f:
            json_data = json.load(f)
            accounts = json_data[account_type]
            for account in accounts:
                result.append(Account(**account))

        return result
