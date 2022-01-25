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

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_breed(self, new_breed):
        self.breed = new_breed

    def get_breed(self):
        return self.breed

    def set_sex(self, new_sex):
        self.sex = new_sex

    def get_sex(self):
        return self.sex

    def set_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

    def set_weight(self, new_weight):
        self.weight = new_weight

    def get_weight(self):
        return self.weight