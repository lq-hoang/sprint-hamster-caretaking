""" Class representing the user account, keeping track of different pet
hamsters, and daily tasks

"""
class User:
    def User(self):
        self.name = ""
        self.hamsters = []

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_Hamsters(self):
        return self.hamsters

