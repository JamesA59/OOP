# Classes and Objects continued

# Execution of a class statement creates a class object and binds it to the class name
# Instantiation of the class creates new instance objects
# Instance objects are first class objects in Python
# Methods are defined inside the class using the def statement
# Inside the method definition the first parameter should be 'self'
# Instance variables can be created inside any method, by assigning to a variable name prefixed with 'self'
#       'print(self.variablename)
# To call a methods inside another method, you have to prefix the method name with 'self'
#       'self.methodname()'

class Person:
    # Self is neessary in the following line
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am ',self.name)

    def greet(self):
        # Self is neessary in the following line
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, how do you do?')
        # Self is neessary in the following line
        self.display()

    # The following function sets the age to 75 
    # Self is neessary in the following line
    def get_old(self):
        self.age = 75

p1 = Person()
p2 = Person()

p1.set_details('Bob', 20)
p2.set_details('Ted',90)

p1.greet()
p2.greet()

p1.get_old()
print(p1.age)