array = [2, 3, 2, 5, 8, 1, 9, 8]
arraytxt = ""
uniq = ""
for i in array:
    arraytxt += str(i) + ' '
for i in array:
    count = array.count(i)
    if count == 1:
        uniq += str(i) + ' '
print(f"Array: {arraytxt}")
print(f"Unique elements: {uniq}")