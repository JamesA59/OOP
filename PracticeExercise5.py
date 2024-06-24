# Practice Exercise 5

class Course:

    def __init__(self, title, instuctor, price, lectures, users, rating, avg_rating):
        self.title = title
        self.instrucor = instuctor
        self.price = price
        self.lecturers = lectures
        self.users = []
        self.rating = rating
        self.avg_rating = avg_rating

    def __str__(self):
        pass

    def new_user_enrolled(self,u):
        self.users.append(u)
        #return self.users

    def received_a_rating(self):
        pass

    def show_details(self):
        pass