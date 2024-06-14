# Inheritance

# Mechanism of creating a new class from an existing class
# The new class is the estended and modified version of the existing class
# Inheritance facilitates code reuse
# Ex. You have a person class with name, age, address, and phone attributes with greet, is_adult, and contact details functions
#       You can have an employee class inherit from the person class all its attributes and functions 
#       and add its own salary, office_address, and office_phone attributes and calculate_tax function
# The person class would be the base class and the employee class would be the derived class
# The Base class is also called the super class or parent class and the derived class is also called the subclass or child class
# The relationship between the derived class and base class is a "is a" relationsip, the employee class "is a " person class
# The derived class gets access to everything from the base class
# Derived classes can override functions (and maybe attributes?) from the base class
# An example would be the employee class having its own contact_details function 
#       that works differently than the person version of contact details function


class Person:
    
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello I am', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False
        
    def contact_details(self):
        print(self.address, self.phone)

class Employee(Person):
    pass

emp = Employee('Jack', 30, 'D4, XYZ Street, Delhi', '9944772291')

print(emp.name)
print(emp.age)
print(emp.address)
print(emp.phone)
emp.greet()
# Should not have to do print() on the below line, but isn't working without it for some reason
print(emp.is_adult())
emp.contact_details()
# Should not have to do print() on the below line, but isn't working without it for some reason
print(isinstance(emp, Employee))
print(isinstance(emp, Person))