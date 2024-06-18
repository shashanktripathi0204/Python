class MyClass:
    def __init__(self, value):
        self.value = value  # Initialize the attribute with a starting value

    # Getter method
    def get_value(self):
        return self.value

    # Setter method
    def set_value(self, new_value):
        self.value = new_value


# Example usage:
obj = MyClass(10)
print(obj.get_value())  # Output: 10

obj.set_value(20)
print(obj.get_value())  # Output: 20
