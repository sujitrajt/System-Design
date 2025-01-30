from vehicle import Vehicle
from levels import ParkingLevel
from typing import List
class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels: List[ParkingLevel] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_level(self, level: ParkingLevel):
        self.levels.append(level)

    def remove_level(self, level: ParkingLevel):
        self.levels.remove(level)
    
    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            spot_number = level.park_vehicle(vehicle)
            if spot_number != -1:
                return spot_number
        return -1
    def unpark_vehicle(self, spot_number):
        for level in self.levels:
            if level.unpark_vehicle(spot_number):
                return True
        return False
    def display_parking_spot(self):
        for level in self.levels:
            level.diplay_parking_spots()

