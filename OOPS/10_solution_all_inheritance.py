# Single Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!


# -----------------------------------------------------------------

# Multiple Inheritance

# Base classes
class A:
    def method_A(self):
        return "Method A"


class B:
    def method_B(self):
        return "Method B"


# Derived class inheriting from A and B
class C(A, B):
    pass


# Example usage
obj = C()
print(obj.method_A())  # Output: Method A
print(obj.method_B())  # Output: Method B

# -----------------------------------------------------------------

# Multilevel Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Unknown sound"


# Intermediate class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Derived class inheriting from Dog
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the immediate parent class
        self.breed = breed

    def play(self):
        return f"{self.name} is playing"


# Creating instances and using them
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!

puppy = Puppy("Charlie", "Pug")
print(puppy.speak())  # Output: Woof!
print(puppy.play())  # Output: Charlie is playing

# -----------------------------------------------------------------

# Hierarchical Inheritance

# Base class
class Animal:
    def speak(self):
        pass

# Derived classes inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# -----------------------------------------------------------------

# Hybrid (Combination) Inheritance

# Base classes
class A:
    def method_A(self):
        return "Method A"

class B(A):
    def method_B(self):
        return "Method B"

# Derived classes using multiple and single inheritance
class C(A):
    def method_C(self):
        return "Method C"

class D(B, C):
    def method_D(self):
        return "Method D"

# Example usage
obj = D()
print(obj.method_A())  # Output: Method A (inherited from A)
print(obj.method_B())  # Output: Method B (inherited from B)
print(obj.method_C())  # Output: Method C (inherited from C)
print(obj.method_D())  # Output: Method D (defined in D)
