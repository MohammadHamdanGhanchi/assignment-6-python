# Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)


# Function to check age and raise the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    else:
        print("Age is valid")


# Testing the function and handling the exception
try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Age must be 18 or older