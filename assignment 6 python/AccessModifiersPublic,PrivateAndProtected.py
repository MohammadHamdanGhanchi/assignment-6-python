class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


# Creating an instance of the Employee class
employee = Employee("Alice", 60000, "123-45-6789")

# Accessing the public variable
print("Name:", employee.name)  # Output: Name: Alice

# Accessing the protected variable
print("Salary:", employee._salary)  # Output: Salary: 60000

# Trying to access the private variable
try:
    print("SSN:", employee.__ssn)
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Employee' object has no attribute '__ssn'

# Accessing the private variable using name mangling
print("SSN")