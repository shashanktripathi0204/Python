class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batter_size):
        super().__init__(brand, model)
        self.battery_size = batter_size


my_tesla = ElectricCar("Tesla", "Model S", "85kwH")

print(my_tesla.model)
print(my_tesla.full_name())
