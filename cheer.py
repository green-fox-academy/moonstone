class cheer:
    def cheer_method(self, member_count, language):
        self.member_count = member_count
        self.language = language
        print(self.member_count)
        print("Moonstone")
        print("hello")
        print(self.language)

teamname = cheer()
teamname.cheer_method(5, "python")
