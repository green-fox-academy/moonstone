class count:

  def ages(self, name):
    self.name = name
    self.current_year = 2017
    self.birth_year = 1986
    self.month = 8
    self.age = self.current_year - self.birth_year
    print("I borned in the: " + str(self.month)+ "th month") 
    if self.age > 50:
      print("I am too old for festivals")
        
count_age = count()
count_age.ages("Tamara")



