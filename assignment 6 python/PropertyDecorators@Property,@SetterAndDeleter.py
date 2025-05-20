class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter method

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price  # Setter method
        else:
            print("Price cannot be negative")

    @price.deleter
    def price(self):
        del self._price  # Deleter method
        print("Price deleted")


# Creating an instance of the Product class
product = Product(100)

# Getting the price
print("Price:", product.price)  # Output: Price: 100

# Setting a new price
product.price = 120
print("New Price:", product.price)  # Output: New Price: 120

# Trying to set a negative price
product.price = -50  # Output: Price cannot be negative
print("Price:", product.price)  # Output: Price: 120

# Deleting the price
del product.price  # Output: Price deleted
try:
    print("Price:", product.price)
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Product' object has no attribute '_price'