# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Derived class


class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Another derived class


class Puppy(Dog):
    def speak(self):
        return "Puppy whines"


# Usage
my_puppy = Puppy()
print(my_puppy.speak())


# Description
# The Puppy class inherits from Dog, which in turn inherits from Animal. This forms a chain of inheritance.
