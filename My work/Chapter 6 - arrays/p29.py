a1 = [4,36,12,28,9,44,5] 
a2 = [5,1,36]
numbers = ""
for i in a1:
    if i not in a2:
        numbers += str(i) + " "
print(numbers)