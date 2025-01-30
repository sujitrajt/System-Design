from seat_enum import SeatStatus, SeatType

class Seat:
    def __init__(self, seat_id, seat_type: SeatType, seat_status: SeatStatus, seat_price, row, column):
        self._seat_id = seat_id
        self._seat_type = seat_type
        self._seat_status = seat_status
        self._seat_price = seat_price
        self._row = row
        self._column = column

    @property
    def get_seat_id(self):
        return self._seat_id
    
    @property
    def get_seat_type(self):
        return self._seat_type
    
    @property
    def get_seat_status(self):
        return self._seat_status
    
    @property
    def get_seat_price(self):
        return self._seat_price
    
    @property
    def get_row(self):
        return self._row
    
    @property
    def get_column(self):
        return self._column
    
    @get_seat_status.setter
    def set_seat_status(self, seat_status):
        self._seat_status = seat_status
    