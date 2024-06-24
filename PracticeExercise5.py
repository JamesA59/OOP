# Practice Exercise 5

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
        print("Title :", self.title, "Instructor: ", self.instrucor, "Price: ", self.price, "Lecturers: ", self.lecturers, 
              "Users: ", self.users, "Ratings: ", self.ratings, "Average Ratings: ", self.avg_rating)

c1 = Course("Project Management", "Ramsower", "$50", "2")
c1.new_user_enrolled("James")
c1.received_a_rating(8)
c1.new_user_enrolled("Natasha")
c1.received_a_rating(7)
c1.show_details()
 