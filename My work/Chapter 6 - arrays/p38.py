real_number = int(input("Enter a number: "))
array = [15, 8, 31, 47, 2, 19, 100, 25, 49, 81, 1, 7, 3, 76]
array.sort()
numbers = ""
count = 0
for i in array:
    count +=1
    if i > real_number:
        if count == len(array):
            numbers += str(i)
        else:
            numbers += str(i) +" "
print(numbers)