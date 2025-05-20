class Logger:
    def __init__(self):
        print("Object created")  # Message when an object is created

    def __del__(self):
        print("Object destroyed")  # Message when an object is destroyed


# Creating an instance of the Logger class
logger = Logger()  # Output: Object created

# Deleting the object
del logger  # Output: Object destroyed