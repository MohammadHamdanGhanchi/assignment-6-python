class Student:
    def __init__(self, name, marks):
        self.name = name  # Assigning the value of 'name' argument to the 'name' attribute of the object
        self.marks = marks  # Assigning the value of 'marks' argument to the 'marks' attribute of the object

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")  # Printing the details of the student


# Creating instances of the Student class
student1 = Student("Alice", 85)
student2 = Student("Bob", 92)

# Calling the display method for each student
student1.display()  # Output: Name: Alice, Marks: 85
student2.display()  # Output: Name: Bob, Marks: 92