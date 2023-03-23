my_text = "Ala ma kota\n"

stripped_text = my_text.strip()
print(stripped_text)

splitted_text = my_text.split()
print(splitted_text)

replaced_text = my_text.replace(" ", "")
print(replaced_text)

joined_text = "---".join(splitted_text)
print(joined_text)

upper_text = my_text.upper()
print(upper_text)

full_name = "jan jans"
names = full_name.split()
print(names)
name = names[0].capitalize()
surname = names[1].capitalize()
print(f"{name} {surname}")
