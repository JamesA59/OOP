# Data Hiding

# In other languages:
# Not all data and methods are made accessible to the user
# The implementation is what is kept private
# While the interface is what is made public to the user
# In Python:
# Everything is made accessible to the user, is product
# Python does allow you to use an underscore before a method or dataset to suggest it should not be used outside it's class
# They still can be used outside their class, but the underscore suggests privacy for them

# Python works on the poilicy that we are all responsible adults
# One of the reasons for making everything public is debugging
# If you prefix a name with a _, it indicates that this name is non public
# If you prefix a name with __, Python will do same name mangling
#       __value becomes _MyClass__value, still accesible but becomes more roundabout
# Names that start and end with two underscores like __init__ are used by Python for its internal use
# A single trailing underscore is used to avoid name clashes with Python built in names

class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20
        self.__data3 = 30

    def methodA(self):
        pass
    
    def _methodB(self):
        pass

    def __methodC(self):
        pass

p = Product()

print(p.data1)
print(p._data2)
#print(p.__data3)
print(p._Product__data3)

p.methodA()
p._methodB()
#p.__methodC()
p._Product__methodC()

# p._data2 and _methodB still run outside of their class, showing they are still accessible
# The underscore is just a naming convention that other programmers should respect and not access outside of their class
#       Unless there is some need for debugging or something similar
# p.__data3 and __methodC don't run outside their class because of the double underscore
# By adding the _Product prefix to data3 and methodC, we can get them to run outside their class
