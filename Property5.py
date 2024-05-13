# Property 5

class Rectangle():
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def diagonal (self):
        return (self.length * self.length + self.breadth * self.breadth) ** 0.5

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length * self.breadth)
    
r = Rectangle(2,5)
# Prints diagonal, area, and perimeter of object created in line 16
print(r.diagonal)
print(r.area())
print(r.perimeter())
# Changes length of object created in line 16 and prints its diagonal, area, and perimeter
r.length = 10
# Diagonal didn't change while it should have, so will make changes so it will update
print(r.diagonal)
print(r.area())
print(r.perimeter())
