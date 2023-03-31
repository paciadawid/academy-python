with open("numbers.txt") as file:
    lines = file.readlines()

total = 0
for number in lines:
    total += int(number)

print(total)
