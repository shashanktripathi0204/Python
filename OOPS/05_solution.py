class Car:
    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Gasoline"


class ElectricCar(Car):
    def __init__(self, brand, model, batter_size):
        super().__init__(brand, model)
        self.battery_size = batter_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kwH")
print(my_tesla.fuel_type())

safari = Car("Tata", "Storm")
print(safari.fuel_type())
