from vehicle import Vehicle
from parking_spot import ParkingSpot
from vehicle_type import VehicleType
from typing import List

class ParkingLevel:
    def __init__(self,floor, num_spots):
        self.floor = floor
        self.parking_spots = List[ParkingSpot] = [ParkingSpot(i) for i in range(num_spots)]
    
    def park_vehicle(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return spot.get_spot_number()
        return -1
        
    def unpark_vehicle(self, spot_number):
        for spot in self.spots:
            if spot.get_spot_number() == spot_number:
                spot.unpark_vehicle()
                return True
        return False
    
    def diplay_parking_spots(self):
        for spot in self.spots:
            print(spot.get_spot_number(), spot.get_vehicle_type())
