class cheer:
   
    def cheer_method(self, member_count, language, cheer_something):
        self.cheer_something = cheer_something
        self.member_count = member_count
        self.language = language
        print(self.member_count)
        print("Moonstone")
        print("hello" + self.cheer_something)
    
    def future(self, params):
        self.params = params
        print("your future looks like " + self.params)

teamname = cheer()
teamname.cheer_method(5, "R2D2", "Greenfox")
teamname.future("happy")

