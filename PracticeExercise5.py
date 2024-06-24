# Practice Exercise 5

'''
1. Create a class named Course that has instance variables 
title, instructor, price, lectures, users(list type), ratings, avg_rating. 
Implement the methods __str__, new_user_enrolled, received_a_rating and show_details. 
From the above class, inherit two classes VideoCourse and PdfCourse. 
The class VideoCourse has instance variable length_video and PdfCourse has instance variable pages.
'''

class Course:

    def __init__(self, title, instuctor, price, lectures):
        self.title = title
        self.instrucor = instuctor
        self.price = price
        self.lecturers = lectures
        self.users = []
        self.ratings = []
        self.avg_rating = 0

    def __str__(self):
        return f'{self.title}, {self.instrucor}, {self.price}, {self.lecturers}'

    def new_user_enrolled(self,u):
        self.users.append(u)
        return self.users

    def received_a_rating(self, r):
        self.ratings.append(r)
        self.avg_rating = sum(self.ratings) / len(self.ratings)
        return self.ratings, self.avg_rating
        

    def show_details(self):
        print("Title :", self.title, "Instructor: ", self.instrucor, "Price: $", self.price, "Lecturers: ", self.lecturers, 
              "Users: ", self.users, "Ratings: ", self.ratings, "Average Ratings: ", self.avg_rating)
        
class VideoCourse(Course):

    def __init__(self, title, instuctor, price, lectures, length_video):
        super().__init__(title, instuctor, price, lectures)
        self.length_video = length_video
        self.users = []
        self.ratings = []
        self.avg_rating = 0

    def __str__(self):
        return f'{self.title}, {self.instrucor}, {self.price}, {self.lecturers}, {self.length_video}'

    def new_user_enrolled(self,u):
        self.users.append(u)
        return self.users

    def received_a_rating(self, r):
        self.ratings.append(r)
        self.avg_rating = sum(self.ratings) / len(self.ratings)
        return self.ratings, self.avg_rating
    
    def show_details(self):
        print("Title :", self.title, "Instructor: ", self.instrucor, "Price: $", self.price, "Lecturers: ", self.lecturers, 
              "Video Length: ", self.length_video, "hours", "Users: ", self.users, "Ratings: ", self.ratings, 
              "Average Ratings: ", self.avg_rating)

class PdfCourse(Course):

    def __init__(self, title, instuctor, price, lectures, pages):
        super().__init__(title, instuctor, price, lectures)
        self.pages = pages
        self.users = []
        self.ratings = []
        self.avg_rating = 0
        
    def __str__(self):
        return f'{self.title}, {self.instrucor}, {self.price}, {self.lecturers}, {self.pages}'

    def new_user_enrolled(self,u):
        self.users.append(u)
        return self.users

    def received_a_rating(self, r):
        self.ratings.append(r)
        self.avg_rating = sum(self.ratings) / len(self.ratings)
        return self.ratings, self.avg_rating
    
    def show_details(self):
        print("Title :", self.title, "Instructor: ", self.instrucor, "Price: $", self.price, "Lecturers: ", self.lecturers, 
              "Pages: ", self.pages, "Users: ", self.users, "Ratings: ", self.ratings, "Average Ratings: ", self.avg_rating)

c1 = Course("Project Management", "Ramsower", 50, 2)
c1.new_user_enrolled("James")
c1.received_a_rating(8)
c1.new_user_enrolled("Natasha")
c1.received_a_rating(7)
c1.show_details()

v1 = VideoCourse("Marketing", "Fernandez", 300, 3, 45)
v1.new_user_enrolled("Ben")
v1.received_a_rating(3)
v1.show_details()

p1 = PdfCourse("Health", "Rogers", 10, 12, 150)
p1.new_user_enrolled("Jake")
p1.received_a_rating(6)
p1.show_details()
 

'''
 2. What is the output of this -
'''
# d.cook will return "Can cook pasta" because Mother is the second base class stated for daughter 
#       and mother's print statement is "Can cook pasta"
# s.cook will return "Can cook butter chicken" because it is his print statement

class Mother:
        def cook(self):
           print('Can cook pasta')
 
class Father:
        def cook(self):
             print('Can cook noodles')
 
class Daughter(Father, Mother):
          pass
 
class Son(Mother, Father):
         def cook(self):
             super().cook()
             print('Can cook butter chicken') 
 
d = Daughter()  
s = Son()
 
d.cook()
print()
s.cook()