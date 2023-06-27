import unittest
from datetime import datetime
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from engine.sternman_engine import SternmanEngine

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
            warning_light_is_on = True

            s = SternmanEngine(warning_light_is_on)
            self.assertTrue(s.needs_service())

    def test_engine_should_not_be_serviced(self):
            warning_light_is_on = False

            s = SternmanEngine(warning_light_is_on)
            self.assertFalse(s.needs_service())    

if __name__ == '__main__':
    unittest.main()