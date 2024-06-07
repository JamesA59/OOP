# Magic Methods 1

# Magic Methods:
# These methods begin and end with double underscore
# Sometimes called dunder methods
# Ex. __init__, __add__, __mul__, __sub__, __eq__, __len__
# Called magic methods as they are run automatically
# Used to overload operators and built in methods
# Magic methods usually aren't called directly, but when thier related syntax is used


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

    # Now that this is a magic method, it specifys the behavior of the instnace objects when they are added together
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
f3 = f1.__add__(f2)
f3.show()
# The line below would not have worked without making the add function a magic method
f3 = f1 + f2
f3.show()
f3 = f1 - f2
f3.show()
f3 = f1 * f2
f3.show()