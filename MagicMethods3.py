# Magic Methods 3

# Reverse and in-place methods
# Have the same spelling of the normal magic methods but start with an r or i
# So __add__ becomes __radd__ or __iadd__

class Fraction:

    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

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
    
    def __radd__(self,other):
        return self.__add__(other)
    
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
f2 = f1 + 3
print(f2)

# The below line will originally not work, since 3 is not a fraction
# By adding the __radd__ function the below line is now able to run
f2 = 3 + f1
print(f2)