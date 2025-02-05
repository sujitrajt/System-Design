from movie import Movie
from user import User
from show import Show

class Booking:
    def __init__(self, booking_id:int, user:User, show:Show, number_of_seats:int):
        self._booking_id = booking_id
        self._user = user
        self._show = show
        self._number_of_seats = number_of_seats

    @property
    def get_booking_id(self):
        return self._booking_id
    
    @property
    def get_user(self):
        return self._user
    
    @property
    def get_show(self):
        return self._show
    
    @property
    def get_number_of_seats(self):
        return self._number_of_seats
    
    @get_number_of_seats.setter
    def set_number_of_seats(self, number_of_seats):
        self._number_of_seats = number_of_seats