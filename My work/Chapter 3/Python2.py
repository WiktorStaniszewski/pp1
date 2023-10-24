def ex1():
    while True:
        try:
            hours = float(input("Enter the number of hours worked: "))
            rate = float(input("Enter the rate you work at: "))
        except ValueError:
            print("Type in a number please. ")
            continue
        else:
            break
    if hours > 40:
        rest = hours - 40
        pay = 40 * rate
        addpay = rest * (1.5*rate)
        fpay = addpay + pay
        print(f"Your pay + overtime pay is: {pay} + {addpay}, {fpay}")
    elif 0 < hours < 40:
        pay = hours*rate
        print(f"Your pay is: {pay}")
    elif hours < 0:
        print("Get to work, you leech")

sum = 0
number = 1
while number <= 5:
  sum = sum + number
  number = number + 1
message = f"Sum of numbers in <1,5> is {sum}"
print(message)
