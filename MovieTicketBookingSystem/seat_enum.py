from enum import Enum

class SeatType(Enum):
    VIP = 1
    Normal = 2
    Sofa = 3

class SeatStatus(Enum):
    Available = 1
    Booked = 2
    Reserved = 3
    NotAvailable = 4

