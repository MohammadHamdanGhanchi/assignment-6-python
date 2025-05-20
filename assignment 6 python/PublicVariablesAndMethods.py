class Car:
    # Public variable
    brand = "Toyota"

    # Public method
    def start(self):
        print("Engine started")


# Creating an instance of the Car class
my_car = Car()

# Accessing the public variable
print("Brand:", my_car.brand)  # Output: Brand: Toyota

# Calling the public method
my_car.start()  # Output: Engine started