class greet:
    def name(self):
        print("I am Zsuzsi")

sample = greet()
sample.name() 

class count:
    def ages(self):
        self.current_year = 2017
        self.birth_year = 1986
        self.age = self.current_year - self.birth_year
        print("My age is: " + str(self.age))

count_age = count()
count_age.ages()

class cheer:
    def cheer_method(self):
        print("Moonstone")

teamname = cheer()
teamname.cheer_method()