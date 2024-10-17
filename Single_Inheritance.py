# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Derived class


class Dog(Animal):
    def speak(self):  # Method overriding
        return "Dog barks"


# Usage
my_dog = Dog()
print(my_dog.speak())  # Output: Dog barks

my_dog = Animal()
print(my_dog.speak())  # Output: Animal speaks

# Descripition
# The Animal class is the base class with a method speak().
# The Dog class inherits from Animal and overrides the speak() method.
