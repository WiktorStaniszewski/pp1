def occurs(number, array):
    if number in list(array):
        return f"Number {number} appears in the array"
    else:
        return "Number not in array"
array = [15, 38, 7, 23, 14]
num = int(input("Enter a Number: "))
print(occurs(num, array))