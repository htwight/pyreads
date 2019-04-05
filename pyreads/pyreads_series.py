class PyReadsSeries(object):
    def __init__(self, series_dict):
        self._series_dict = series_dict
    
    @property
    def id(self):
        return self._series_dict['id']

    @property
    def title(self):
        return self._series_dict['title']

    @property
    def description(self):
        return self._series_dict['description']

    @property
    def note(self):
        return self._series_dict['note']

    @property
    def series_works_count(self):
        return self._series_dict['series_works_count']

    @property
    def primary_work_count(self):
        return self._series_dict['primary_work_count']

    @property
    def numbered(self):
        return self._series_dict['numbered']

    @property
    def series_work(self):
        return self._series_dict['series_work']