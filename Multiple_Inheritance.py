# Base class 1
class Canine:
    def bark(self):
        return "Woof!"

# Base class 2


class Pet:
    def play(self):
        return "Playing with the pet"

# Derived class


class Dog(Canine, Pet):
    def speak(self):
        return "Dog barks"


# Usage
my_dog = Dog()
print(my_dog.bark())
print(my_dog.play())

# Description
# The Dog class inherits from both Canine and Pet, allowing it to access methods from both base classes.
