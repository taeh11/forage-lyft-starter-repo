import unittest
from datetime import datetime
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from engine.capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
            current_mileage = 30001
            last_service_mileage = 0

            capulet = CapuletEngine(current_mileage, last_service_mileage)
            self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
            current_mileage = 30000
            last_service_mileage = 0

            capulet = CapuletEngine(current_mileage, last_service_mileage)
            self.assertFalse(capulet.needs_service())    

if __name__ == '__main__':
    unittest.main()