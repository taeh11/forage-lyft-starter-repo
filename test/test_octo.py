import unittest
from datetime import datetime
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from tires.octo import Octo

class TestOcto(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_array = [0.5, 0.5, 1, 1]

        tire = Octo(tire_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_array = [0, 0.5, 0.8, 0.4]

        tire = Octo(tire_array)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()