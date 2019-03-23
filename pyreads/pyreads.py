from requests_oauthlib import OAuth1Session

class PyReads(object):
    def __init__(self, client_key, client_secret):
        self.client_key = client_key
        self.client_secret = client_secret
        self.oauth = self.session()
    
    def session(self):
        return OAuth1Session(self.client_key, client_secret=self.client_secret)

    def request(self, url):
        return self.oauth.get(url)