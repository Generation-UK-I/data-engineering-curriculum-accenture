import unittest
from docking_station import *

class TestDockingStation(unittest.TestCase):
    
    def test_init(self):
        name = "Central Station"
        capacity = 5
        station1 = DockingStation(name, capacity)
        self.assertEqual(name, station1.station_name)
        self.assertEqual(capacity, station1.station_capacity)
        self.assertEqual([], station1.bikes)