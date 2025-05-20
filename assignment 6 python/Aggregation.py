class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Employee Name: {self.name}, ID: {self.employee_id}")


class Department:
    def __init__(self, name, employee=None):
        self.name = name
        self.employee = employee  # Aggregation: Department "has-a" Employee (but Employee can exist independently)

    def set_employee(self, employee):
        self.employee = employee

    def display_department_info(self):
        print(f"Department Name: {self.name}")
        if self.employee:
            self.employee.display_employee_info()
        else:
            print("No employee assigned to this department.")


# Creating an instance of the Employee class
employee1 = Employee("Alice", "101")

# Creating an instance of the Department class
department1 = Department("Sales")

# Aggregating the Employee object with the Department object
department1.set_employee(employee1)

# Displaying the department information
department1.display_department_info()
# Output:
# Department Name: Sales
# Employee Name: Alice, ID: 101

# Demonstrating that the Employee object exists independently
employee1.display_employee_info()
# Output:
# Employee Name: Alice, ID: 101