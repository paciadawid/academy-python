for i in range(1, 11):
    print(i)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

a = 0
while a < 10:
    print(a)
    a += 1

b = 0
while True:
    print(b)
    if b > 10:
        break
    b += 1

for i in range(10, 100, 2):
    print(i)

a = 10
while a < 100:
    print(a)
    a += 2

n = 4
if n == 0:
    result = 1
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
print(f"Factorial from {n} equals {result}")

isbn = "030640615"
