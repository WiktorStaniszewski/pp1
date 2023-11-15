array = [[1, 3, 5], [8, 7, 2]]
print(array[0][0]+array[1][2])
print(array[0][len(array)//2]+array[1][len(array)//2])
sum = 0
for i in array[1][0:3]:
    sum +=i
print(sum)
