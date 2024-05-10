# __init__ method

# Initialization work is done automatically by Python if you define __init__ method
# You create and initialize all your instance variables in this method
# YOu can also perfrom any other initialization tasks
# The first parameter to __init__ is always self
# Other parameters are used to give initial values ot instance variables
# There are other dudner methods also having special names
# To construct an instance, the __new__magic method is invoked 
# __init__ is the initializer method
# You can have only one __init__ in a class

# __init__ is called a 'dunder init', Python will implicitly call it, so you don't have to 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am ',self.name)

    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, how do you do?')

# The set_details method has to be called to give the name and age attributes values or else it will create an error
# Unless a dunder init is used instead
# If a dunder init is used, you insert the values for the object into the parenthesis when the object is crated
p1 = Person('John',20)
p1.display()
p1.greet()

p2 = Person('Jack',90)
p2.display()
p2.greet()