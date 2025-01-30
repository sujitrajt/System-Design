from datetime import datetime
from typing import Dict, List
from movie import Movie
from theater import Theater
from seat import Seat
from show import Show
from booking import Booking
from itertools import count

class MovieTicketBookingSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.movies = []
            cls._instance.theater = []
            cls._instance.shows = {}
            cls._instance.bookings = {}
            cls._instance.booking_counter = itertools.count(1)
        return cls._instance
    
    @staticmethod
    def get_instance():
        if MovieTicketBookingSystem._instance is None:
            MovieTicketBookingSystem()
        return MovieTicketBookingSystem._instance
    
    def add_movie(self, movie:Movie):
        self.movies.append(movie)
    
    def add_theater(self, theater:Theater):
        self.theater.append(theater)

    def add_show(self, show:Show):
        self.shows[show.get_show_id] = show

    def get_movie(self):
        return self.movies
    
    def get_theater(self):
        return self.theater
    
    def book_ticket(self, user:User, show:Show, selected_seats:List[Seat]):
        if self._are_seats_available(show, selected_seats):
            self._mark_selected_seats(show, selected_seats)
            total_price = self._calulate_price(selected_seats)
            booking_id = next(self.booking_counter)
            booking = Booking(booking_id, user, show, selected_seats)
            self.bookings[booking_id] = booking
            return booking
        return None
    