""" Class representing the user account, keeping track of different pet
hamsters, and daily tasks

"""
import Hamster

class User:
    def __init__(self):
        self.name = ""
        self.hamsters = []
        self.tasks = []

    def __int__(self, name, hamsters, tasks):
        self.name = name
        self.hamsters = hamsters
        self.tasks = tasks

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_hamsters(self):
        return self.hamsters

    def set_hamsters(self, new_list):
        self.hamsters = new_list