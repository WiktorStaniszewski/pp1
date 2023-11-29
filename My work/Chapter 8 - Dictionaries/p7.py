person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person["name"])
print(person["hobby"])
print(person["married"])
person["married"] = not person["married"]
person["gender"] = "male"
person["hobby"] += ["bicycle"]
person["phone"]["work"] = "313131444"
print(person["hobby"])
print(person["gender"])
print(person["phone"])
