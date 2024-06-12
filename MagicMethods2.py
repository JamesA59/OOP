# Magic Methods 2

# a == b -> a.__eq__(b)
# a != b -> a.__ne__(b)
# a < b -> a.__lt__(b)
# a > b -> a.__gt__(b)
# a <= b -> a.__le__(b)
# a >= b -> a.__ge__(b)

# a.__str__()
# a.__repr__()

class Fraction:

    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def __str__(self):
        return f'{self.nr}/{self.dr}'
    
    def __repr__(self):
        return f'Fraction({self.nr}, {self.dr})'
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr , self.dr * other.dr)
        f._reduce()
        return f
    
    def __eq__(self, other):
        return (self.nr * other.dr) == (self.dr * other.nr)
    
    def __lt__(self, other):
        return (self.nr * other.dr) < (self.dr * other.nr)
    
    def __le__(self, other):
        return (self.nr * other.dr) <= (self.dr * other.nr)
    
    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        
        self.nr //= h
        self.dr //= h

    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
    
f1 = Fraction(2,3)
f2 = Fraction(3,4)
print(f1 == f2)
print(f1 != f2)

f2 = Fraction(2,3)
f3 = Fraction(4,6)

print(f1 == f2)
print(f1 == f3)
print(f1 != f2)

f3 = Fraction(1,5)

print(f1 < f2)
print(f1 <= f2)
print(f3 < f1)

f = Fraction(2,3)
# The 2 lines below doesn't give 2/3 value without str function
# Have to use show function to give 2/3 value
print(f)
print(str(f))
f.show()

f1 = Fraction(3,4)
f2 = Fraction(2,3)
f3 = Fraction(6,7)
L = [f1,f2,f3]
# Line below doesn't give values of fractions without __repr__ function
print(L)