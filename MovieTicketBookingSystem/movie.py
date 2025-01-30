class Movie:
    def __init__(self, movide_id, name, description, duration):
        self._movie_id = movide_id
        self._name = name
        self._description = description
        self._duration = duration
    
    @property
    def get_duration(self):
        return self._duration
    