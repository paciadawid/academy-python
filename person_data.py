person_string = "hcl:5d90f0 cid:270"

records = person_string.split()

person_dict = {}
for record in records:
    key, value = record.split(":")
    person_dict[key] = value

print(person_dict)
