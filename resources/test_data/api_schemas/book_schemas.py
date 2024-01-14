class BookSchemas:

    book_success_response_schema = {
        "isbn": str,
        "title": str,
        "subTitle": str,
        "author": str,
        "publish_date": str,
        "publisher": str,
        "pages": int,
        "description": str,
        "website": str,
    }
