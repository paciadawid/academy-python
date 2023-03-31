class Animal:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def print_name(self):
        print(self.name)


class Cat(Animal):

    def __init__(self, breed, name):
        super().__init__(name)
        self.breed = breed

    def calculate_food(self, mass):
        return mass * 7


class Person:

    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth

    def print_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_age(self):
        age = 2023 - self.year_of_birth
        return age

    def change_surname(self, new_surname):
        self.surname = new_surname


class Student(Person):

    def __init__(self, name, surname, year_of_birth, grades=[]):
        super().__init__(name, surname, year_of_birth)
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return round(sum(self.grades) / len(self.grades))
