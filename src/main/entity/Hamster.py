""" Class representing individual "profiles"
for hamsters under a user's ownership.
"""


class Hamster:
    def __init__(self, name: str, breed: str, sex: str, age: [int], weight: float, notes: str):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.weight = weight
        self.notes = notes

    def display_profile(self) -> str:
        profile = "Name:", self.name, "\nBreed:", self.breed, "\nSex:", self.sex, \
                  "\nAge:", self.age, "\nWeight (g):", self.weight, \
                  "\nNotes:", self.notes
        return profile

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def get_name(self) -> str:
        return self.name

    def set_breed(self, new_breed: str) -> None:
        self.breed = new_breed

    def get_breed(self) -> str:
        return self.breed

    def set_sex(self, new_sex: str) -> None:
        self.sex = new_sex

    def get_sex(self) -> str:
        return self.sex

    def set_age(self, new_age: str) -> None:
        self.age = new_age

    def get_age(self) -> [int]:
        return self.age

    def set_weight(self, new_weight: float) -> None:
        self.weight = new_weight

    def get_weight(self) -> float:
        return self.weight

    def set_notes(self, new_note: str) -> None:
        self.notes = new_note
