arr = [8, 2, 5, 1, 9]
count = 0
for i in arr:
    i **= 2
    arr[count] = i
    count+=1
print(arr)