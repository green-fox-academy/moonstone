class greet:
    def name(self, name, age, school):
        self.school = school
        self.name = name
        self.age = age
        print("Greetings from " + self.name + " i am " + self.age + " years old.")
        print("Greetings for the " + self.school)


sample = greet()
sample.name("Zsuzsi", "25", "Green Fox") 
