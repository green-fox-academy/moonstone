class count:

  def ages(self, name):
    self.name = name
    self.current_year = 2017
    self.birth_year = 1986
    self.age = self.current_year - self.birth_year
    print("My age is: " + str(self.age))
    print(self.name)
    if self.age > 50:
      print("I am too old for festivals")
        
count_age = count()
count_age.ages("Tamara")



