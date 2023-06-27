import unittest
from datetime import datetime
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from engine.willoughby_engine import WilloughbyEngine

class TestW(unittest.TestCase):
    def test_engine_should_be_serviced(self):
            current_mileage = 60001
            last_service_mileage = 0

            w = WilloughbyEngine(current_mileage, last_service_mileage)
            self.assertTrue(w.needs_service())

    def test_engine_should_not_be_serviced(self):
            current_mileage = 60000
            last_service_mileage = 0

            w = WilloughbyEngine(current_mileage, last_service_mileage)
            self.assertFalse(w.needs_service())    

if __name__ == '__main__':
    unittest.main()