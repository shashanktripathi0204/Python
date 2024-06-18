# Static method are accessed withing the class but not by the object

class Car:

    total_car = 0

    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.model = model
        # we can access this using self.total_car also
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Gasoline"

    @staticmethod
    def general_description():
        return "Car are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model, batter_size):
        super().__init__(brand, model)
        self.battery_size = batter_size

    def fuel_type(self):
        return "Electric Charge"


# we can access static method using class objects but it is recommended not to do so
my_car = Car("Tata", "Safari")
print(my_car.general_description())
