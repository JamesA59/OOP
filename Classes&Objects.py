# Classes and Objects

# Class names usually begin with and uppercase letter and are singular nouns, can use cammelcase for multiple words
# pass is used to give no info to the class
# def is a function, they say what the objects assigned to the class do
# self is almost always a parameter in every function
# The class object is created when the class definition is executed
# In a method definition, the parameter "self" refers to the instance object that invokes the method
# Instantation of the class creates a new instance object

class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am ',self.name)

    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, how do you do?')
        self.display()

p1 = Person()
p2 = Person()

# This gives p1 and p2 the name and age attributes and sets them
p1.set_details('Bob', 20)
p2.set_details('Ted',90)

# This gives p2 it's own name and age, another way of changing them
#p2.name = 'Jack'
#p2.age = 30

# Performs display and greet functions of p1 and p2
#p1.display()
p1.greet()
#p2.display()
p2.greet()

# prints the name and age of p1 and p2
#print(p1.name)
#print(p1.age)
#print(p2.name)
#print(p2.age)
