class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


# Object of car is my_Car
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

# Object of car is my_new_car
my_new_Car = Car("Tata", "Safari")
print(my_new_Car.brand)
print(my_new_Car.model)