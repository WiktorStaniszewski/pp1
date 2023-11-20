arr = [15, 8, 31, 47, 2 , 19]
count = 0
sum = 0
for i in arr:
    count += 1
    sum += i
print(arr)
amean = sum/count
print(round(amean, 2))