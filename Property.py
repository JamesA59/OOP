# Property

# A property allows access to an instance variable through methods, even though the method syntax is not used
# @property - to be placed before the getter method
# @name.setter - to be placed before the setter method
# @name.deleter - to be placed before the deleter method
# Attribute type checking and validation
# Crate a read only or write only attribute
# Transform an instance variable into a dynamically calculated attribute
# Incorporate a new bahviour in your instance variables, without any need to rewrite the existing client code

class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

# '@property' is a decorator
# When we decorate a method with this line, that method can be accessed like an instance
    @property
    def value(self):
        return self._x
    
    # This will let us assign a value to p.value
    @value.setter
    def value(self,val):
        self._x = val

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,val):
        self._y = val

p = Product(12,24)

# This line will print the x value, the parenthesis are necessary
#print(p.value())

# Now that the @property decorator is there, we no longer need the parenthesis
# Prints original x value set in line 30, and that value plus 2
print(p.value)
print(p.value+2)

# Before adding the '@value.setter' decorator, this line wouldn't run
# While a new attribure had be defined, it could only be referenced and can't assign a value to it
# Sets x value to 10 and prints it
p.value = 10
print(p.value)

# 1st line prints original y value set in line 30
# Second and third lines sets that y value to 12 and prints that
print(p.y)
p.y = 12
print(p.y)