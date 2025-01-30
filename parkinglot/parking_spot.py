from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.vehicle_type = VehicleType.CAR
        self.parked_vehicle = None

    def is_available(self):
        return self.parked_vehicle is None
    
    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise Exception("Invalid vehicle or spot already taken")
        
    def unpark_vehicle(self):
        if self.parked_vehicle is not None:
            self.parked_vehicle = None
        else:
            raise Exception("No vehicle parked at this spot")
    
    def get_spot_number(self):
        return self.spot_number
    
    def get_vehicle(self):
        return self.parked_vehicle
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def get_vechicle_license_plate(self):
        return self.parked_vehicle.license_plate
    
