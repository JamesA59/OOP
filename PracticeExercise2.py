# Practice Exercise 2

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    #def set_details(self, name, balance=0):
        #self.name = name
        #self.balance = balance

    def display(self):
        print("The account belonging to ", self.name, " has a balance of $", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        if 50 < price < 1000:
            self.price = price
        else:
            raise ValueError('Price must be between 50 and 1000')
        self.copies = copies

    def display(self):
        print(self.isbn, self.title, self.price, self.copies)

    def in_stock(self):
        if self.copies > 0:
            print("True")
        else:
            print("False")
    
    def sell(self):
        if self.copies > 0:
            self.copies -= 1
        else: 
            print("The book is out of stock.")

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

books = [book1, book2, book3, book4]


for i in books:
    i.display()


JackBooks = []

x = 0
for i in books:
    if books[x].author == "Jack":
        JackBooks.append(books[x].title)
    x = x + 1

print(JackBooks)

class Fraction:
     
    def __init__(self, nr, dr=1):
        self.nr = nr
        if dr > 0:
             self.dr = dr
        else:
            self.dr = dr * -1

    def show(self):
        print(self.nr, "/", self.dr)

    def multiply(self, other):
        nr = self.nr * other.nr
        dr = self.dr * other.dr
        return Fraction(nr,dr)
    
    def add(self, other):
        nr = self.nr * other.dr + other.nr * self.dr
        dr = self.dr * other.dr
        return Fraction(nr,dr)

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
# Fix this for problem 7
#f3 = f1.add(5) 
#f3.show()
#f3 = f1.multiply(5) 
#f3.show()

class Product():

    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        if marked_price <500:
            self.discount = discount
        else:
            self.discount = discount +2
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)

    @property
    def selling_price(self):
        print(round(self.marked_price * 100 / (100 - self.discount),2))
    
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

print(p1.selling_price)
print(p4.selling_price)

class Circle():

    def __init__(self, radius):
        self.radius = radius
        self._diameter = round(self.radius * 2,2)
        self._circumfrence = round(2 * 3.14 * self.radius,2)
        self._area = round(3.14 * self.radius * self.radius,2)

    @property
    def diameter(self):
        return self._diameter

    @property
    def circumfrence(self):
        return self._circumfrence

    def area(self):
        return self._area

c1 = Circle(5)

print(c1.diameter)
print(c1.circumfrence)
print(c1.area)