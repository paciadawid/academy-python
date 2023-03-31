def add_one(value):
    result = value + 1
    return result


def calculate_fuel(mass):
    if type(mass) not in [int, float]:
        return None

    if mass <= 0:
        return None

    fuel = mass // 3 - 2

    if fuel <= 0:
        return 1

    return fuel

# 1/2 -> 0 in python 2
# 1/2 -> 0.5 in python 3
