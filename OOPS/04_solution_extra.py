# accessing the private variable in parent class directly from child class without using get method

class Car:
    def __init__(self, brand):
        self.__brand = brand  # private variable


class ElectricCar(Car):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity

    def get_car_details(self):
        # Accessing the private variable of the parent class
        return f"Brand: {self._Car__brand}, Battery Capacity: {self.battery_capacity}"


# Usage
my_car = ElectricCar("Tesla", "100 kWh")
print(my_car.get_car_details())  # Output: Brand: Tesla, Battery Capacity: 100 kWh