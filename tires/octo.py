from tires.tire import Tire


class Octo(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        sum = 0
        for i in self.tire_wear_array:
            sum += i

        if sum >= 3:
            return True
        else:
            return False
