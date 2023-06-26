from abc import ABC, abstractmethod
from datetime import date 

from serviceable import Serviceable
from engines import *
from batteries import *
from car import Car


class CarFactory():

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(current_mileage, last_service_mileage), Spindler(current_date, last_service_date))
        
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), Spindler(current_date, last_service_date))
        
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        return Car(SternmanEngine(warning_light_on), Spindler(current_date, last_service_date))
        
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), Nubbin(current_date, last_service_date))

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(current_mileage, last_service_mileage), Nubbin(current_date, last_service_date))