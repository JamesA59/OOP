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

    names = []
    total_revenue = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)
 
    def make_sale(self,money):
        self.sales_amount += money
        SalesPerson.total_revenue += money
 
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
 
s1.show()
s2.show()
s3.show()

print(SalesPerson.names)
print(SalesPerson.total_revenue)

class Employee: 

    Domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self,name,email):
        self.name = name
        self.email = email
        domain = email[email.index('@')+1 : ]
        Employee.Domains.add(domain)

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        domain = new_email[new_email.index('@')+1 : ]
        if domain in Employee.allowed_domains:
            self._email = new_email
        else:
            raise RuntimeError(f'Domain {domain} is not allowed')

    def display(self):
        print(self.name, self.email)
            
e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@gmail.com')
e6 = Employee('Mike','mike@yahoo.com')

print(Employee.Domains)
'''
e4.email = 'ted@ymail.com'
e4.display()
'''
 
e3.email = 'jill@gmail.com'
e3.display()


'''
class Stack:    

    MAX_SIZE = 7

    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def size(self):
        return len(self.items)
 
    def push(self, item):
        if self.size == Stack.MAX_SIZE:
            raise RuntimeError("Stack is full")
        self.items.append(item)
 
    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()
    
    def display(self):
        print(self.items)
 
if __name__ == "__main__":
    st = Stack()
 
    while True:
        print("1.Push") 
        print("2.Pop") 
        print("3.Peek") 
        print("4.Size")
        print("5.Display") 
        print("6.Quit")
         
        choice = int(input("Enter your choice : "))
 
        if choice == 1:
            x=int(input("Enter the element to be pushed : "))
            st.push(x) 
        elif choice == 2:
            x=st.pop() 
            print("Popped element is : " , x) 
        elif choice == 3:
            print("Element at the top is : " , st.peek()) 
        elif choice == 4:
            print("Size of stack " , st.size()) 
        elif choice == 5:
            st.display()         
        elif choice == 6:
          break;
        else:
          print("Wrong choice") 
        print() 
'''


class BankAccount:
 
    bank_name = "Chase"

    def __init__(self, name, balance=0, bank=bank_name):
        self.name = name
        self.balance = balance
        self.bank = bank
        
    def display(self):
         print(self.name, self.balance, self.bank)
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
    
a1 = BankAccount('Mike', 200)
a2 = BankAccount('Tom')
 
a1.display()
a2.display()