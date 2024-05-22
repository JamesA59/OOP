# Class Variables

class Person:

    # This variable, species, is defined inside the class, but outside any method, so it is a class variable
    # A class variable is shared by all instances of the class
    # It belongs to the class, not to individual instance objects
    # Class variables are generally placed at the top of the class definition, just below the class header
    species = 'Homo Sapiens'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # This will increase the class variable by 1 for each new instance created
        # This variable will not different for each object, but will update for all objects with the creation of each new object
        # ex. Once object p4 is created, p1.count will equal to 4, not 1
        Person.count +=1

    # Class variables an also be referenced 
    def display(self):
        print(f'{self.name} is {self.age} years old')

p1 = Person('John', 20)
p2 = Person('Jack', 34)

p1.display()
p2.display()

'''
print(Person.species)
print(p1.species)
print(p2.species)
'''

# All the above refrences refer to the same variable as shown through the below three lines
'''
print(id(Person.species))
print(id(p1.species))
print(id(p2.species))
'''

print(Person.count)

# These two new instances will increase the count from 2 to 4
p3 = Person('Jill', 40)
p4 = Person('Jane', 35)
print(Person.count)

class BankAccount:

    rate_of_interest = 5
    # In an example like this, minimum balance could be used in the withdraw function
    minimum_balance = 100
    minimum_balance_fees = 10
    
    def __init__(self,account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount('7348', 'Tom', 50)
account2 = BankAccount('6378', 'Bob', 400)

class Book():

    # If the instance variable has the same name as the class variable, 
    # then the instance variable hides the class variable if you access the name through an instance
    # In this example there is both a class and instance variable named x
    # This can be seen in the results of the code written in lines 87-89
    x = 5

    def __init__(self):
        self.x = 100

    def display(self):
        print(self.x)
        print(Book.x)

b = Book()
b.display()
print(Book.x)
print(b.x)

# In the following example, I will show what happens when you try to change a class variable in an instance

class Account():
    
    rate = 5

    # Created last
    # Shows how trying to change the class variable like this just creates a different variable
    def some_method(self):
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))
        #self.rate = 10
        Account.rate = 10
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))

a1 = Account()
a2 = Account()
'''
print(Account.rate)
print(a1.rate)
print(a2.rate)

# When we change the value of the variable here, it changes for the class and all objects
Account.rate = 6
print(Account.rate)
print(a1.rate)
print(a2.rate)

# While it looks like I was able to change the variable of one object, 
# while not changing the value of the variable for the class itself or other objects
a1.rate = 7
print(a1.rate)
print(Account.rate)
print(a2.rate)

# All it did was create a new instance variable as shwon in the below lines
print(id(Account.rate))
print(id(a1.rate))
print(id(a2.rate))
'''

# This goes with the some_method method and it's notes
# The id for account rate stays the same, but the id for self rate changes, showing a whole new variable was created
# The above line was typed when some_method was changing self.rate and not account.rate
# Now the account.rate is changed, self.rate and account.rate reference the same variable in their own line, shown by matching ids
a1.some_method()