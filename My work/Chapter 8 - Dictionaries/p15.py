basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

person= {}

for key, value in basic_data.items():
    person[key] = value

for key, value in advanced_data.items():
    person[key] = value

for key, value in person.items():
    if type(value) == list:
        print(f"{key}   : ")
        for i in value:
            print(f"             {i}")
    else:
        print(f"{key:<10} : {value:<10}")