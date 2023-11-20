a = [True,False]   
b = [True,False,True]
array1 = ""
array2 = ""
for i in a:
    array1 += str(i) + " "
for i in b:
    array2 += str(i) + " "
print(f"Array1 = {array1}") 
print(f"Array2 = {array2}")
if a==b:
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")