import json
import os


class Book():
    def __init__(self, book_name):
        self.book_name = book_name

    @classmethod
    def get_list_book_from_json(cls, json_file_path, book_type):
        result = []
        with open(os.path.abspath(json_file_path)) as f:
            data = json.load(f)
            list_json_book = data[book_type]
            for json_book in list_json_book:
                result.append(Book(**json_book))
            
        return result
