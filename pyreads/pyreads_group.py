class PyReadsGroup(object):
    def __init__(self, group_dict):
        self._group_dict = group_dict

    @property
    def id(self):
        return self._group_dict['id']

    @property
    def title(self):
        return self._group_dict['title']

    @property
    def description(self):
        return self._group_dict['description']

    @property
    def access(self):
        return self._group_dict['access']

    @property
    def location(self):
        return self._group_dict['location']

    @property
    def last_activity_at(self):
        return self._group_dict['last_activity_at']

    @property
    def display_folder_count(self):
        return self._group_dict['display_folder_count']
    
    @property
    def display_topics_per_folder(self):
        return self._group_dict['display_topics_per_folder']
    

    @property
    def add_books_flag(self):
        return self._group_dict['add_books_flag']
    

    @property
    def polls_flag(self):
        return self._group_dict['polls_flag']
    

    @property
    def discussion_public_flag(self):
        return self._group_dict['discussion_public_flag']
    

    @property
    def real_world_flag(self):
        return self._group_dict['real_world_flag']
    

    @property
    def accepting_new_members_flag(self):
        return self._group_dict['accepting_new_members_flag']
    

    @property
    def bookshelves_public_flag(self):
        return self._group_dict['bookshelves_public_flag']
    

    @property
    def category(self):
        return self._group_dict['category']
    

    @property
    def subcategory(self):
        return self._group_dict['subcategory']
    

    @property
    def rules(self):
        return self._group_dict['rules']