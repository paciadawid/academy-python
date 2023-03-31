with open("people_data.txt", "r") as file:
    lines = []
    for line in file.readlines():
        lines.append(line.strip())

people_list = []
person_dict = {}
for line in lines:
    if line:
        records = line.split()
        for record in records:
            key, value = record.split(":")
            person_dict[key] = value
    else:
        people_list.append(person_dict)
        person_dict = {}
