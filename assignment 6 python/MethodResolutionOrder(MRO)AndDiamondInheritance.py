class A:
    def show(self):
        print("A's show()")


class B(A):
    def show(self):
        print("B's show()")


class C(A):
    def show(self):
        print("C's show()")


class D(B, C):
    pass


# Creating an instance of D
d = D()

# Calling show() on the instance of D
d.show()  # Output: B's show()

# Displaying the MRO of class D
print(D.mro())
# Output:
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]