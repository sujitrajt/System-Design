from abc import ABC
from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_type(self):
        return self.vehicle_type
    