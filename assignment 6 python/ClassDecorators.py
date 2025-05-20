def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"

    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


# Creating an instance of the decorated class
person = Person("Alice")

# Calling the new greet() method
print(person.greet())  # Output: Hello from Decorator!