class Person:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def display_name(self):
        print(f"Name: {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the Person class
        self.subject = subject  # Initialize the subject attribute

    def display_details(self):
        super().display_name()  # Call the display_name method of the Person class
        print(f"Subject: {self.subject}")


# Creating an instance of the Teacher class
teacher = Teacher("Bob", "Math")

# Calling the display_details method
teacher.display_details()
# Output:
# Name: Bob
# Subject: Math