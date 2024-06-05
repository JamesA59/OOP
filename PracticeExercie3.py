# Practice Exercie 3

class Fraction:
     
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if dr > 0:
             self.dr = dr
        else:
            self.dr = dr * -1
        self._reduce()

    def show(self):
        print(self.nr, "/", self.dr)

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.nr , self.dr * other.dr)
    
    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
    
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

f1 = Fraction(6,36)
f1.show()
f2 = Fraction(2,-12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()

class SalesPerson:   

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sales_amount = 0
 
    def make_sale(self,money):
        self.sales_amount += money
 
    def show(self):
        print(self.name, self.age, self.sales_amount)
 
s1 = SalesPerson('Bob', 25)
s2 = SalesPerson('Ted', 22)
s3 = SalesPerson('Jack', 27)
 
s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)

SalesPeople = [s1,s2,s3]
total_revenue = 0
names = []
names = [i.name for i in SalesPeople]
for i in SalesPeople:
    total_revenue += i.sales_amount
 
s1.show()
s2.show()
s3.show()

print(names)
print(total_revenue)