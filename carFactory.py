from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import Nubbin
from battery.spindler import Spindler


class CarFactory():

    def create_calliope(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(current_mileage, last_service_mileage), Spindler(current_date, last_service_date))
        
    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), Spindler(current_date, last_service_date))
        
    def create_palindrome(current_date, last_service_date, warning_light_on: bool):
        return Car(SternmanEngine(warning_light_on), Spindler(current_date, last_service_date))
        
    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), Nubbin(current_date, last_service_date))

    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(current_mileage, last_service_mileage), Nubbin(current_date, last_service_date))