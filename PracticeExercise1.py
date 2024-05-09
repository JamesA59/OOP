# Practice Exercise 1

class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print("The account belonging to ", self.name, " has a balance of $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

a1 = BankAccount()
a2 = BankAccount()

a1.set_details("James", 0)
a2.set_details("Sarge", 0)

a1.deposit(10000)
a2.deposit(200)

a1.withdraw(150)
a2.withdraw(100)

a1.display()
a2.display()