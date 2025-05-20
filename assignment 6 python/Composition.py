class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"Engine type {self.engine_type} started")


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Car "has-a" Engine

    def start(self):
        print(f"Car model {self.model} starting...")
        self.engine.start()  # Accessing the Engine's start method


# Creating an instance of the Engine class
engine = Engine("V8")

# Creating an instance of the Car class, passing the Engine object
car = Car("Mustang", engine)

# Calling the Car's start method, which in turn calls the Engine's start method
car.start()
# Output:
# Car model Mustang starting...
# Engine type V8 started
