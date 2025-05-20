class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable for the dog's name
        self.breed = breed  # Instance variable for the dog's breed

    def bark(self):
        print(f"{self.name} says Woof!")  # Instance method to make the dog bark, including its name


# Creating instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

# Calling the bark method for each dog
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Lucy says Woof!