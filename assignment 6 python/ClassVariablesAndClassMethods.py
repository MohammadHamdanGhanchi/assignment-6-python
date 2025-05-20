class Bank:
    # Class variable
    bank_name = "XYZ Bank"

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# Creating instances of the Bank class
bank1 = Bank()
bank2 = Bank()

# Printing the initial bank name
print("Bank 1 Name:", bank1.bank_name)  # Output: Bank 1 Name: XYZ Bank
print("Bank 2 Name:", bank2.bank_name)  # Output: Bank 2 Name: XYZ Bank

# Changing the bank name using the class method
Bank.change_bank_name("ABC Bank")

# Printing the updated bank name for both instances
print("Bank 1 Name:", bank1.bank_name)  # Output: Bank 1 Name: ABC Bank
print("Bank 2 Name:", bank2.bank_name)  # Output: Bank 2 Name: ABC Bank