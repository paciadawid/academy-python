class Animal:

    def __init__(self, name):
        self.name = name

    def set_a_name(self, new_name):
        self.name = new_name

    def print_name(self):
        print(self.name)

    def get_name(self):
        return self.name


class Cat(Animal):

    def __init__(self, breed, name):
        super().__init__(name)
        self.breed = breed

    def calculate_food(self, mass):
        return mass * 7


pajton = Cat("dachowiec", "Pajton")
pajton.print_name()
print(f"Food needed: {pajton.calculate_food(4.5)}")



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

# jan = Person("Jan", "Testowy", 1999)
# jan.print_full_name()
# jan.change_surname("Nietestowy")
# jan.print_full_name()
# print(jan.get_age())
