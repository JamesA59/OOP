# Property 4

class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    # This property is read only because it only has a getter method (property?)
    @property
    def name(self):
        return self._name
    # This property is write only because the getter method raises an error and also has a setter method
    @property
    def password(self):
        raise AttributeError('password not readable')
    
    @password.setter
    def password(self, new_password):
        self._password = new_password

    # This property is read and write because it has both a getter and a setter method
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        self._password = new_salary

e = Employee('Jill', 'feb31', 5000)

# Prints the name of the object created in line 31
print(e.name)
# Attempts to change the name to 'xyz' but creates an error due to the property being read only, so it will be ignored
#e.name = 'xyz'

# Attemps to print the password of the object created in line 31, 
# but can't because property is write only and raised an error due to line 16, so will be ignored
#print(e.password)
# Sets password for object created in line 31 to 'abc'
e.password = 'abc'

# Prints salary of object created in line 31
print(e.salary)
# Changes salary of object created in line 31 and prints it
e.salary = 6000
print(e.salary)