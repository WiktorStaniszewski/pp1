names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
for i in names:
    if i == names[0]:
        x = i
    else:
        if len(i) > len(x):
            x = i
print(x)