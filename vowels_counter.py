my_text = "Ala ma kota"
#text_lower = my_text.lower()

vowels = "aeiouy"

counter = 0
for letter in my_text:
    if letter in vowels or letter in vowels.upper():
        counter += 1
print(counter)
