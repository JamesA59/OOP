# Property 2

class Person:

    def __init__(self, name, age):
        self.name = name
        #self._age = age
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError('Age must be between 20 and 80')

    def display(self):
        print(self.name, self._age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')
        
    def get_age(self):
        return self._age

if __name__ == '__main__':
    p = Person('Raj', 30)
    p.display()

# Should give an error because age is not between 20 and 80, as set to do in line 20
#p.set_age(100)

# Should work because age is between 20 and 80
p.set_age(25)
p.display()

# Increases age by 1
p.set_age(p.get_age()+1)
p.display()

# Creating an object like this circumvents the restirction created in line 20
# So lines 8-11 were added and line 7 is now ignored
# Now this code doesn't work, so it will ignored
#p1 = Person('Dev', 200)
#print(p1.display())

