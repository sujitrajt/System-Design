from theater import Theater
from seat import Seat
from typing import Dict
from datetime import datetime
from movie import Movie
class Show:
    def __init__(self,show_id, movie:Movie, theater:Theater, start_time:datetime, end_time:datetime, seats:Dict):
        self._show_id = show_id
        self._movie = movie
        self._theater = theater
        self._start_time = start_time
        self._end_time = end_time
        self._seats = seats

    @property
    def get_show_id(self):
        return self._show_id
    
    @property
    def get_movie(self):
        return self._movie
    
    @property
    def get_theater(self):
        return self._theater
    
    @property
    def get_start_time(self):
        return self._start_time
    
    @property
    def get_end_time(self):
        return self._end_time
    
    @property
    def get_seats(self):
        return self._seats
    
    # @get_seats.setter
    # def set_seats(self, seats):
    #     self._seats = seats