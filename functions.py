def add_one(value):
    result = value + 1
    return result


def calculate_fuel(mass):
    # fuel = math.floor(mass / 3) - 2
    # fuel = int(mass / 3) - 2
    fuel = mass // 2 - 2
    return fuel


print(calculate_fuel(14))


# 1/2 -> 0 in python 2
# 1/2 -> 0.5 in python 3
