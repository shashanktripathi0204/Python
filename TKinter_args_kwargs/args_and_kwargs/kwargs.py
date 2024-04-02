def calculate(**kwargs):
    print(kwargs)
    for key, values in kwargs.items():
        print(key,values)


calculate(add = 3, multiply = 5)

# ----------------------------------------------------------------------------------------------------------------------

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make = "Nissan", model = "GT-R")
print(my_car.model)