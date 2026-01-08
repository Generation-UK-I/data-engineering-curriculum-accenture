from docking_station import *

class Bike:
    
    def __init__(self, name):
        self.bike_name = name
        
    def dock_at_station(self, station):
        if len(station.bikes) == station.station_capacity:
            raise DockingStationException("This docking station is already at capacity")
        station.bikes.append(self)
        
    def undock_from_station(self, station):
        station.bikes.remove(self)
