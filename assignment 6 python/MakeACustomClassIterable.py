class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value


# Creating an instance of the Countdown class
countdown = Countdown(5)

# Iterating over the Countdown object
for num in countdown:
    print(num)
# Output:
# 5
# 4
# 3
# 2
# 1