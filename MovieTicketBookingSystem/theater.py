from typing import List

class Theater:
    def __init__(self, theater_id, name, location, shows: List):
        self._theater_id = theater_id
        self._name = name
        self._location = location
        self._shows = shows

    @property
    def get_theater_id(self):
        return self._theater_id
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_location(self):
        return self._location
    
    @property
    def get_shows(self):
        return self._shows
    