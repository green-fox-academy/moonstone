class cheer:
    def cheer_method(self, member_count):
        self.member_count = member_count
        print(self.member_count)
        print("Moonstone")

teamname = cheer()
teamname.cheer_method(5)
