class count:

  def ages(self, name, number, birth_year):
    self.name = name
    self.current_year = 2017
    self.birth_year = birth_year
    self.month = 8
    self.number = number
    self.age = self.current_year - self.birth_year
    print(self.age)
    print("I borned in the: " + str(self.month)+ "th month in " + str(self.birth_year))
    print("Counting the countless: " + str(self.number))
    print("I borned in the: " + str(self.month)+ "th month") 

    if self.age > 50:
      print("I am too old for festivals")
        
count_age = count()
count_age.ages("Tamara", 12, 1986)



