from basics.classes import Student


andrzej = Student("Andrzej", "Nietestowy", 1999)

assert andrzej.get_age() == 25, f"Andrzej has {andrzej.get_age()} years, not 25."


fruits = ["apple", "orange"]

assert "apple" in fruits, ""
