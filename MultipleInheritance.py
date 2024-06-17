# Multiple Inheritance

# There can be multipled derived classes from a single base class
# One derived class can inherit from multiple base classes
#       coded as: class X(A,B,C):
                        #pass
# Ex. class TeachingAssistant(Student, Teacher):
            # pass

'''
class Teacher:
    
    def greet(self):
        print("I am a Teacher")

class Student:
    def greet(self):
        print("I am a Student")

class TeachingAssistant(Student, Teacher):
        #print("I am a Teaching Assistant")
        pass


x = TeachingAssistant()
# When the print function within the TeachingAssistant class is ignored, the print function below will print 'I am a Student'
# from the Student class because Student is listed before teacher is the parenthesis for the TeachingAssistant class
# If they were reveresed the line below would print 'I am a Teacher'
# It shouldn't print 'none' after 'I am a Teacher' or 'I am a Student'
print(x.greet())

# Below line shows all bases classes of a derived class
print(TeachingAssistant.__bases__)
'''

# Diamond Inheritance is when two derived classes from a single base class are the base classes for a single derived class
# Ex. Student and Teacher classes are derived from a Person base class,
#  and a TeachingAssistant class is derived from the Student and Teacher base classes
# Technically Person would also be derived from the object class, making it four levels deep
# Creating a structure having multi-level and multiple inheritance

# Method Resoltuion Order (RMO)
# Order in which Python searches for attributes in base classes
# RMO computed using C3 linearization algorithm
#       Works in a left to right manner, searching each class once
# To see MRO of a class:
    #classname.__mro__
    # classname.mro()
    # help(classname)
    # instance.__class__.__mro__


class Person:
    def greet(self):
        print('I am a Person')
    # pass

class Teacher(Person):
    
    def greet(self):
        print("I am a Teacher")
    # pass

class Student(Person):
    
    def greet(self):
        print("I am a Student")
    #pass

class TeachingAssistant(Student, Teacher):
   
    def greet(self):
        print("I am a Teaching Assistant")
    #pass

x = TeachingAssistant()
x.greet()
help(TeachingAssistant)
# To see lines after the above line will have to go to terminal and press enter, maybe a few tmes
# Shouldn't have to use print on the below lines,  but not working without it
print(TeachingAssistant.__mro__)
print(TeachingAssistant.mro())
print(x.__class__.__mro__)

# After ignoreing the greet function for TeacherAssistant, it printed "I am a Student" again
# I then ignored the greet function for Student, it printed "I am a Teacher"
# To ensure there are no errors for this section ignore the for instances of these classes and the lines that go with them
# I then ignored the greet function for Teacher, it printed "I am a Person"
# I then ignored the greet function for Person and got an error because Object class does not have a greet function