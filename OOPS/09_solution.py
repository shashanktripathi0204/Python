# Static method are accessed withing the class but not by the object

class Car:
    total_car = 0

    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.__model = model
        # we can access this using self.total_car also
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Gasoline"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, batter_size):
        super().__init__(brand, model)
        self.battery_size = batter_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85 KWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))