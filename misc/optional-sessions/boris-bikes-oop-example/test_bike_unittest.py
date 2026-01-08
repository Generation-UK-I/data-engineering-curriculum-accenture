import unittest
from bike import *

class TestBike(unittest.TestCase):
    
    def test_init(self):
        name = "Colin's Bike"
        bike1 = Bike(name)
        self.assertEqual(name, bike1.bike_name)
    
    def test_should_dock_bike(self):
        bike1 = Bike("test bike")
        station1 = DockingStation("test station", 5)
        
        bike1.dock_at_station(station1)
        
        self.assertEqual(1, len(station1.bikes))
        self.assertEquals(station1.bikes[0], bike1)
    
    def test_should_undock_bike(self):
        bike1 = Bike("test bike")
        station1 = DockingStation("test station", 5)
        station1.bikes.append(bike1)
        
        bike1.undock_from_station(station1)
        
        self.assertEqual(0, len(station1.bikes))
        self.assertEquals(station1.bikes, [])
        
    def test_should_not_dock_bike_if_station_at_capacity(self):
        bike1 = Bike("test bike")
        bike2 = Bike("another test bike")
        station1 = DockingStation("test station", 1)
        bike1.dock_at_station(station1)
        
        with self.assertRaises(DockingStationException):
            bike2.dock_at_station(station1)