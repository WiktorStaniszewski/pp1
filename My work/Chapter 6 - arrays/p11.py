def month(n):
    month_name = ["January", "February", "March", "April", "July", "June", "July", "August", "September", "October", 'November', 'December']
    if int(n)<=0:
        return "No month '0'"
    else:
        n-=1
    return month_name[n]

number = int(input("Enter a month number: "))
print(month(number))