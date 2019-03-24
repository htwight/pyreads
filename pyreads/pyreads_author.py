class PyReadsAuthor(object):
    def __init__(self, author_dict):
        self._author_dict = author_dict['author']

    @property
    def id(self):
        return self._author_dict['id']

    @property
    def name(self):
        return self._author_dict['name']

    @property
    def fans_count(self):
        return self._author_dict['fans_count']['#text']

    @property
    def followers_count(self):
        return self._author_dict['author_followers_count']['#text']
    
    @property
    def about(self):
        return self._author_dict['about']

    @property
    def influences(self):
        return self._author_dict['influences']

    @property
    def works_count(self):
        return self._author_dict['works_count']

    @property
    def gender(self):
        return self._author_dict['gender']

    @property
    def hometown(self):
        return self._author_dict['hometown']

    @property
    def born_at(self):
        return self._author_dict['born_at']

    @property
    def died_at(self):
        return self._author_dict['died_at']