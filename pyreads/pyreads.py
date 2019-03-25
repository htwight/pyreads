from requests_oauthlib import OAuth1Session
from pyreads_author import PyReadsAuthor
from pyreads_book import PyReadsBook
import xmltodict

class PyReads(object):
    def __init__(self, client_key, client_secret):
        self.client_key = client_key
        self.client_secret = client_secret
        self.oauth = self.session()
    
    def session(self):
        return OAuth1Session(self.client_key, client_secret=self.client_secret)

    def request(self, url, payload={}):
        payload['key'] = self.client_key
        payload['format'] = 'xml'
        return self.oauth.get(url, params=payload)

    def author(self, author_id):
        r = self.request(f"https://www.goodreads.com/author/show/{author_id}").text
        author = xmltodict.parse(r)
        author_dict = author['GoodreadsResponse']['author']
        return PyReadsAuthor(author_dict)

    def book(self, isbn):
        r = self.request(f"https://www.goodreads.com/book/isbn/{isbn}?").text
        book = xmltodict.parse(r)
        book_dict = book['GoodreadsResponse']['book']
        return PyReadsBook(book_dict)

    def book_by_id(self, book_id):
        r = self.request(f"https://www.goodreads.com/book/show/{book_id}.xml").text
        book = xmltodict.parse(r)
        book_dict = book['GoodreadsResponse']['book']
        return PyReadsBook(book_dict)