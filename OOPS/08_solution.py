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


# we can access static method using class objects, but it is recommended not to do so
my_car = Car("Tata", "Safari")


# print(my_car.model()) -- this will throw an error as our decorator has made it a property instead of a method

print(my_car.model)
# first we need to make it private
