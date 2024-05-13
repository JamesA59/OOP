# Property 3

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')

if __name__ == '__main__':
    p = Person('Raj', 30)
    p.display()

# Prints age as 30 as set in line 24
print(p.age)
# Sets age as 34, no errors
p.age = 34
# Attempts to set age as 100, but creates error due to lines 18-21, will now be ignored
#p.age = 100

# Attempts to create a new object under the Person class, with a name of Dev and an age of 200
# Creates error due to lines 18-21, will now be ignored
#p1 = Person('Dev',200)

# Two different ways of increasing the age by 1
p.age = p.age + 1
p.age += 1
print(p.age)