""" Class representing individual "profiles"
for hamsters under a user's ownership.
"""


class Hamster:
    def __init__(self, name, breed, sex, age, weight=-1, notes=""):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.weight = weight
        self.notes = notes

    def display_profile(self):
        return ("Name:", self.name, "\nBreed:", self.breed, "\nSex:", self.sex,
                "\nAge:", self.age, "\nWeight (g):", self.weight,
                "\nNotes:", self.notes)

    def set_weight(self, new_weight):
        self.weight= new_weight
