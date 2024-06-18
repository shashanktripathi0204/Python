class Car:
    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batter_size):
        super().__init__(brand, model)
        self.battery_size = batter_size


my_tesla = ElectricCar("Tesla", "Model S", "85kwH")

# print(my_tesla.__brand)
print(my_tesla.get_brand())
