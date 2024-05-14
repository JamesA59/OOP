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
            self._price = price
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

#for x in books:
    #if "Jack" in x:
        #JackBooks.append(x)

#print(JackBooks)