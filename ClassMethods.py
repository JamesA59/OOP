# Class Methods

class MyClass():
    a = 5

    def __init__(self, x):
        self._x = x

    def method1(self):
        print(self.x)

    # If you add the below line before a method, it becomes a class method
    # The first parameter in a class method is cls
    # A class method can work only with class variables
    @classmethod
    def method2(cls):
        print(cls.a)

MyClass.method2()

'''
class Person:

    species = 'Homo Sapiens'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count +=1

    def display(self):
        print(f'{self.name} is {self.age} years old')

    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} {cls.species}')

# The 'Person.show_count()' lines will show if 35-38 works
Person.show_count()

p1 = Person('John', 20)
p2 = Person('Jack', 34)

Person.show_count()

# Can also work like this:
p1.show_count()
'''

# The most common use of class methods is to define factory methods
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name, self.age, 'years old')

    @classmethod
    def from_str(cls,s):
        name,age = s.split(',')
        return cls(name, int(age))
    
    @classmethod
    def from_dict(cls,d):
        return cls(d['name'], d['age'])

p1 = Person('John', 20)
p2 = Person('Jack', 34)

# Can use class methods as factory methods to create instance objects in different ways
# Can create instances of class Person from different types of data:
s = 'Jim, 23'
p3 = Person.from_str(s)
p3.display()

d = {'name': 'Jane', 'age':34 }
p4 = Person.from_dict(d)
p4.display()

