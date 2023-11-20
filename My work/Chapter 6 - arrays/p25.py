arr = [15, 8, 31, 47, 2 , 19]
count = 0
sum = 0
while count != len(arr):
    sum += arr[count]
    count += 1
amean = sum/count
print(arr)
print(round(amean, 2))
