employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]

names = list(filter(lambda x:x[0].upper(), employees))
print(names)