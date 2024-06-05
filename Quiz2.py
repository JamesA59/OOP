# Quiz 2

# 1. Instance variables are unique to each instance, Class variables are shared by all intances of the class

# 2. Variables that are assigned a value in class definition are class variables, 
# and variables that are assigned values inside class methods are instance variables

# 3. False - If you call a class method using an instance arguement, it receives the instance as the first arguement
# Class method always receives the class as the first arguement, whether it is invoked through the class or through the instance

# 4. Conventionally the first parameter of an instance method is named self and the first parameter of a class method is named cls

# 5. The @classmethod decorator changes the method such that it receives the class as the first argument 
# and @staticmethod decorator changes the method such that it receives no special first arguement

# 6. In a class method, you can use any word instead of cls, it could be self also. 
# But never do this as it is unconventional and confusing

# 7. You can not write an instance variable with the class name, 
# for example MyClass.x where MyClass is the name of the class and x is an instance variable

# 8. You can write a class variable preceded with an instance name, 
# for example p1.x where p1 is the name of an instance and x is a class variable