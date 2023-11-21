tup = (10,20,30,40,50) 
print(tup)
sectup = []
for i in tup[::-1]:
    sectup.append(i)
sectup = tuple(sectup)
print(sectup)