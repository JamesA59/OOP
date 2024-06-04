# Static Methods

# Methods:
# Instance Methods - To make a method that needs access to instance variables
# Class Methods - To make a method that needs to use only class variables
# Static Methods - To make a method that needs to use neither class variables nor instance variables

class MyClass():

    a = 5
    def __init__(self, x):
        self.x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)

    # Static methods don't have any special first parameters
    # When you have to create a helper or utility method, that contains some logic related to the class, turn it into a static mehtod
    @staticmethod
    def method3(m,n):
        return m+n
    
