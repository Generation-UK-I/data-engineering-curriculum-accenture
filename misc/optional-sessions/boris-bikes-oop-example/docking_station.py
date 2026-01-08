class DockingStation:
    
    def __init__(self, name, capacity):
        self.station_name = name
        self.station_capacity = capacity
        self.bikes = []
        
        
class DockingStationException(Exception):
    pass
