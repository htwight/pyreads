class PyReadsBook(object):
    def __init__(self, book_dict):
        self._book_dict = book_dict

    @property
    def id(self):
        return self._book_dict['id']

    @property
    def title(self):
        return self._book_dict['title']

    @property
    def isbn(self):
        return self._book_dict['isbn']

    @property
    def isbn13(self):
        return self._book_dict['isbn13']

    @property
    def kindle_asin(self):
        return self._book_dict['kindle_asin']

    @property
    def marketplace_id(self):
        return self._book_dict['marketplace_id']

    @property
    def country_code(self):
        return self._book_dict['country_code']

    @property
    def publication_year(self):
        return self._book_dict['publication_year']

    @property
    def publication_month(self):
        return self._book_dict['publication_month']

    @property
    def publication_day(self):
        return self._book_dict['publication_day']

    @property
    def publisher(self):
        return self._book_dict['publisher']

    @property
    def language_code(self):
        return self._book_dict['language_code']

    @property
    def is_ebook(self):
        return self._book_dict['is_ebook']

    @property
    def description(self):
        return self._book_dict['description']