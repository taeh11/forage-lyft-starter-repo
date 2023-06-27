import unittest
from datetime import datetime
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from battery.nubbin import Nubbin

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nubbin = Nubbin(today, last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        nubbin = Nubbin(today, last_service_date)
        self.assertFalse(nubbin.needs_service())

if __name__ == '__main__':
    unittest.main()