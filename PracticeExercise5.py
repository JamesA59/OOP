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

# d.cook will return "Can cook noodles" because Father is the first base class stated for daughter 
#       and father's print statement is "Can cook noodles"
# Then there will be a blank line
# s.cook will return "Can cook pasta" because Mother is the first base class stated for son 
#       and mother's print statement is "Can cook pasta" 
#       then "Can cook butter chicken" because it is son's print statement

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

'''
3. What will be the output of this code -
'''

# x.greet will return "I am Person" because it is the print statement of the base class of the class Teaching Assistant is derived from
        # Then it will return "I am Student" because it is the print statement of Teaching Assistant's base class
        # and listed before the other base class 'Teacher' when initializing the TeachingAssistant class
        # Finally, it will return "I am a Teaching Assistant" because it is Teaching Assistant's own print statement

class Person:
    def greet(self):
        print('I am a Person')
 
class Teacher(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')
 
class Student(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Student')
 
class TeachingAssistant(Student, Teacher):
     def greet(self):
         super().greet()
         print('I am a Teaching Assistant')
       
x = TeachingAssistant()
x.greet()

'''
4. In the following inheritance hierarchy we have written code to add 'S' to id of Student, 
'T' to id of Teacher and both 'T' and 'S' to id of Teaching Assistant.
 What will be the output of this code. If the code does not work as intended, what changes we need to make.
'''

# From what I can tell, the issue with the code is that it is only adding the 'T' and not the 'S' to the Teaching Assistant id
# This is because using base class names can cause bugs with multiple inheritance, can fix this by using super()
# Will add this fix to the Teacher, Person, and TeachingAssistant classes



class Person:
    def __init__(self,id):
        self.id = id
        
class Teacher(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'T'

# Original
'''
class Teacher(Person):
    def __init__(self,id):
        Person.__init__(self,id)
        self.id += 'T'
'''
    
class Student(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'S'

# Original
'''
class Student(Person):
    def __init__(self,id):
        Person.__init__(self,id)
        self.id += 'S'
'''
   
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        super().__init__(id)

# Original
'''
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        Student.__init__(self,id)
        Teacher.__init__(self,id)
'''
       
x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)