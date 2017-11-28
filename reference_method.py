class greet:
    def name(self, name, age, school):
        self.school = school
        print("Greetings from " + name + " i am " + age + " years old.")
        print("Greetings for the " + self.school)


sample = greet()
sample.name("Zsuzsi", 25, "Green Fox") 
