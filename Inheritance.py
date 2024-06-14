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
    
    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05
        
    def contact_details(self):
        Person.contact_details(self)
        print(self.office_address, self.office_phone)

emp = Employee('Jack', 30, 'D4, XYZ Street, Delhi', '9944772291', 8000, 'ABC Street, Delhi', '897865589')

# Below lines through 'issubclass' were done before anything was added to Employee, it was just passed
print(emp.name)
print(emp.age)
print(emp.address)
print(emp.phone)
emp.greet()
# Should not have to do print() on the below line, but isn't working without it for some reason
print(emp.is_adult())
emp.contact_details()
# Should not have to do print() on the below lines, but isn't working without it for some reason
# isinstance lines show that emp is an instance of both employee and person classes, 1st and 2nd true
# issubclass line shows that employee is a derived class of the person base class, 3rd true
print(isinstance(emp, Employee))
print(isinstance(emp, Person))
print(issubclass(Employee, Person))
# Every class in python inherits from a base class called object as shown below, 4th true
print(issubclass(Person, object))
# All types (like int and str) are names of classes as shown below, 5th and 6th true
print(issubclass(int, object))
print(issubclass(str, object))

print(emp.salary)
print(emp.calculate_tax())
# Below line shows contact details function being overwritten within the Employee class from the Person class, has 2 lines
emp.contact_details()