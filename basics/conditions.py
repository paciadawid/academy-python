a = 10
b = 1

if a > 0:
    print("Value is positive")
elif a == 0:
    print("Value is zero")
elif a < 10:
    print("Value is negative")
else:
    print("Something went wrong")

if a > 0 and b > 0:
    print("Both values positive")
elif a > 0 or b > 0:
    print("One value is positive")

a = [0]
if a:  # 0, (), [], {}, "", None -> False
    print("This is True")
else:
    print("This is False")
