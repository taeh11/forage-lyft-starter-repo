from tires.tire import Tire



class Carrigan(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        for i in self.tire_wear_array:
            if i >= 0.9:
                return True
        return False
