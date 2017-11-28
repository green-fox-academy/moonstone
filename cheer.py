class cheer:
    def cheer_method(self, member_count, parameter):
        self.member_count = member_count
        print(self.member_count)
        print("Moonstone")
        print("hello")
        print("Cheer for " + parameter)
    
    def future(self, params):
        print("your future looks like " + params)

teamname = cheer()
teamname.cheer_method(5, "R2D2")
teamname.future("happy")


