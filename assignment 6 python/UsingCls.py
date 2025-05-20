class Counter:
    count = 0  # Class variable to keep track of the number of objects

    def __init__(self):
        Counter.count += 1  # Increment the count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")  # Display the current count


# Creating instances of the Counter class
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

# Calling the class method to display the count
Counter.display_count()  # Output: Number of objects created: 3