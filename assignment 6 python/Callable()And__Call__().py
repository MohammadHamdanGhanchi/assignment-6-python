class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x


# Creating an instance of the Multiplier class
multiplier = Multiplier(5)

# Testing if the object is callable
print("Is callable:", callable(multiplier))  # Output: Is callable: True

# Calling the object like a function
result = multiplier(10)
print("Result:", result)  # Output: Result: 50