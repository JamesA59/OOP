# MRO and Super

# MRO = Method Resolution Order
# When overriding functions with using inheritence, can use super to refer to base classes attributes and functions
# As seen here:
'''

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
        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05
        
    def contact_details(self):
        super().contact_details()
        print(self.office_address, self.office_phone)

'''

# This can get more confusing when using multiple inheritance though
# This code would originally be be lines with, listing I am a teacher, student, teacherassistant, and person twice
# By changing the code and adding super(), am able to have it say 'I am a person' only once
# Super follows MRO

class Person:

    def greet(self):
        print('I am a Person')

class Teacher(Person):
    
    def greet(self):
        #Person.greet(self)
        super().greet()
        print("I am a Teacher")

class Student(Person):
    
    def greet(self):
        #Person.greet(self)
        super().greet()
        print("I am a Student")

class TeachingAssistant(Student, Teacher):
   
    def greet(self):
        #Student.greet(self)
        #Teacher.greet(self)
        super().greet()
        print("I am a Teaching Assistant")

x = TeachingAssistant()
x.greet()

#help(TeachingAssistant)

s = Student()
s.greet()

help(Student)

# Super makes the code more maintainable
# In a situation where you change the name of the base class, you wouldn't need to change the .greet function in every derived class