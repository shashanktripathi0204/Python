# Proteced Variables

class MyClass:
    def __init__(self):
        self._protected_value = 10  # Protected variable

    def _protected_method(self):
        return self._protected_value  # Protected method


obj = MyClass()

print(obj._protected_value)  # Output: 10
print(obj._protected_method())  # Output: 10