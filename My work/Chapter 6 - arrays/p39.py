array = [15, 8, 31, 47, 2, 19, 100, 25, 49, 81, 1, 7, 3, 76, 12, 24, 36, 58]
array.sort()
even = []
odd = []
for i in array:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)