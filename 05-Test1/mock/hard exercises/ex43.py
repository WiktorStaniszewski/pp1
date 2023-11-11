n1 = 0
n2 = 1
next_number = n2
n = int(input("Enter the amount of number: "))
i = 0
allnums = str(n1) + f" {str(n2)}"
while i < n-2:
    next_number = n1+n2
    allnums += f" {str(next_number)}"
    n1 , n2 = n2, next_number
    i += 1
print(allnums)