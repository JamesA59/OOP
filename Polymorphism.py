# Polymorphism

# 3 main features of OOP:
# Encapsulation
# Inheritance
# Polymorphism

# Polymorphism - the ability to take many forms
# Polymorphism - Ability of code to take different forms depending on the type with which it is used
# Ex. 
#       def do_something(x):
#           x.move()
#           x.stop()
# Function will only work correctly if we send objects thats data type support the move and stop functions


# All 3 of these classes have the functions 'move' and 'stop' and the implementation is different in all of them

class Car:

    def start(self):
        print('Engine started')

    def move(self):
        print('Car is running')

    def stop(self):
        print('Brakes applied')


class Clock:

    def move(self):
        print('Tick Tick Tick')

    def stop(self):
        print('Clock needles stopped')


class Person:

    def move(self):
        print('Person walking')

    def stop(self):
        print('Taking rest')

    def talk(self):
        print('Hello')


car = Car()
clock = Clock()
person = Person()

def do_something(x):
    x.move()
    x.stop()

do_something(car)
do_something(clock)
do_something(person)

# This is polymorphism, the same code taking different forms

# All 3 of these classes have the functions 'area' and 'perimeter' and the implementation is different in all of them
# They all also have a class variable called 'name'

class Rectangle:
    
    name = 'Rectangle'

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    

class Triangle:

    name = 'Triangle'

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        sp = (self.s1 + self.s2 + self.s3) / 2
        return (sp * (sp - self.s1) * (sp - self.s2) * (sp - self.s3))
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    

class Circle:

    name = 'Cirlce'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

r1 = Rectangle(13, 25)
r2 = Rectangle(14,16)
t1 = Triangle(14,17,12)
t2 = Triangle(25, 33, 52)
c1 = Circle(14)
c2 = Circle(25)

def find_area_perimeter(shape):
    print(shape.name)
    print('Area: ', shape.area())
    print('Perimeter: ', shape.perimeter())

# line below gives wrong output
find_area_perimeter(t2)
find_area_perimeter(c1)
find_area_perimeter(r2)

# Still need to fix triangle area
shapes = [r1, r2, t1, t2, c1, c2]
total_area = 0
total_perimeter = 0
for shape in shapes:
    total_area += shape.area()
    total_perimeter += shape.perimeter()
print(total_area, total_perimeter)

# Polymorphism does not depend on inheritance
# For polymorphism to occur you just need to define different classes which have commonly named methods
# Python's polymorphism is based on duck typing:
#       'If it walks like a duck, and quacks like a duck, then it is a duck'
# So different objects that have common method names, can be treated in the same general way
# Benefits of polymorphism:
#       You can write generic code that can work with objects of different classes
#       Polymorphism makes your code concise and flexible
#       The code is easy to update, you can easily add new types 
#           For example, can add rhombus class with area and perimeter functions
#       The behaviour shown by overloaded operators is polymorphism
#           For example, the data can behave different ways based off of the data types in the below lines
#               def func(a, b):
#                   print(a + b)
#                   print(a * b) 