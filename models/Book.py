import json
import os


class Book:
    def __init__(self, book_name, isbn):
        self.book_name = book_name
        self.isbn = isbn

    @classmethod
    def get_list_book_from_json(cls, json_file_path, book_type):
        result = []
        with open(os.path.abspath(json_file_path)) as f:
            json_data = json.load(f)
            books = json_data[book_type]
            for book in books:
                result.append(Book(**book))

        return result
