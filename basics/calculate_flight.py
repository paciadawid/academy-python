destination = "Nicosia"

destinations = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Gdansk": 480,
    "Chartum": None
}

distance = destinations[destination]

if distance:
    cost = distance * 2

    if 0 < distance < 2000:
        cost += 100

    # if distance >= 2000:
    #     cost = distance * 2
    # elif 2000 > distance > 0:
    #     cost = distance * 2 + 100

    print(f"Total cost to {destination} is {cost}")
else:
    print(f"No trip to {destination}")
