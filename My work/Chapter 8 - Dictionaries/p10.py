import json
with open("data.json") as kfc:
    data = json.load(kfc)

for i in data:
    for key,value in i.items():
        if key == "contact" or key == "studies" or key == "languages":
            print(f"{key}:  ")
            for n in value:
                if n == "email" or n == "courses":
                    for m in n:
                        print(f"        {m}")
                else:
                    print(f"    {n}")

        else:
            print(f"{key} : {value}")




'''
napisz funkcje ktora na podstawie nazwy kraju, 
zwroci liczbe osob z tego kraju

if n == "email" or n == "phone" or n == "semester" or n == "field" or n == "fulltime" or n == "courses":
                else:
'''