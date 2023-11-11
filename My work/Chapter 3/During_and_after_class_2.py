def ex8():
    speed_limit = 140
    while True:
        try:
            car_speed = int(input('Enter car speed km/h: '))
        except ValueError:
            print("Type in an integer.")
            continue
        else:
            break
    if car_speed > speed_limit:
        print('Warning: speed limit exceeded!!')
    elif car_speed < speed_limit:
        print("Congrats!, You're driving safely")

def ex9():
    while True:
        try:
            result = int(input("Enter your points on the test: "))
            max = int(input("Enter the maximum amount of points: "))
        except ValueError:
            print("Error. Type in an integer.")
            continue
        else:
            break
    percentage = result/max*100
    percentage = round(percentage)
    if percentage > 50:
        print("You passed!", end=" ")
        print(f"You scored: {percentage}%")
    else:
        print("You failed!", end=" ")
        print(f"You scored: {percentage}%")

def ex10():
    while True:
        try:
            number = int(input("Enter a negative number: ")) 
        except ValueError:
            print("Error. Type in an integer.")
            continue
        else:
            break
    print(f"The absolute value of {number} is {abs(number)}")

def ex11():
    number = int(input("Enter a number: "))
    if number%2 != 0:
        print("The number is odd")
    else:
        print("The number is even")

def ex12():
    name1 = input("Enter the first person's name: ")
    age1 = int(input("Enter the first person's age: "))
    name2 = input("Enter the second person's name: ")
    age2 = int(input("Enter the second person's age: "))
    if age1 >= 18 and age2 >= 18:
        print(f"Both {name1} and {name2} are adults")

def ex13():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    if no1 >= 0 or no2 >= 0:
        print("At least one of the entered number is not negative")
    else:
        print("Both numbers are negative")

def ex14():
    i = 0
    while i<=4:
        print("Practice makes perfect")
        i += 1
def ex15():
    for i in range(5):
        print("Practice makes perfect")

def ex16():
    for number in range(1,6):
        print(number)
        number += 1

def ex17():
    i = 1
    sum = 0
    while i <= 5:
        print(i)
        sum += i
        i += 1
    print(sum)

def ex181():
    z = 1
    while z <= 10:
        print(1/z)
        z += 1
def ex182():
    i = 1
    for i in range(1,11):
        print(1/i)
        i += 1

def ex19():
    sum = 0
    for i in range(1,11):
        print(i)
        i += 1
        if i%2 == 0:
            sum += i
    print(sum)

def ex21():
    while True:
        try:
            no1 = int(input("Enter a number: ")) 
            no2 = int(input("Enter a second number: "))
        except ValueError:
            print("Error. Type in an integer.")
            continue
        else:
            break
    numbers = [no1, no2]
    print(f"Numbers in ascending order: {sorted(numbers)}")

def ex22():
    name = input("Enter a name: ")
    print(name[-1])
    if name[-1] == "a" or name[-1] == "A":
        print(f"{name} is a female name")
    else:
        print(f"{name} is not a female name")

def ex23():
    while True:
        try:
            dogyear = float(input("Enter your dog's age: "))
        except ValueError:
            print("Error. Enter a number.")
            continue
        else:
            break
    if dogyear <= 2:
        humanyears = dogyear*10.5
        print(humanyears)
    elif dogyear > 2:
        remainder = dogyear - 2
        firstyears = 2*10.5
        restyears = remainder*4
        humanyears = firstyears + restyears
        print(humanyears)

def ex24():
    while True:
        try:
            cpp = float(input("Enter the current price: "))
            ppp = float(input("Enter the previous price: "))
        except ValueError:
            print("Error. Enter a number.")
            continue
        else:
            break
    diff = cpp/ppp*100
    discount = 100-diff
    if discount >= 10:
        print("Buy the product!!")
        print(f"The price has gone down by {int(discount)}%")
    else:
        print(f"Not worth buying yet, only {int(discount)}% price reduction")

def ex25():
    while True:
        try:
            number = int(input("Enter the number of products purchased: "))
        except ValueError:
            print("Error. Enter an integer.")
            continue
        else:
            break
    liszt = []
    if number <= 2:
        for i in range(1, 3):
            while True:
                try:
                    price = float(input("Please enter a price: "))
                except ValueError:
                    print("Error. Enter an integer.")
                    continue
                else:
                    break
            liszt.append(price)
            house = sum(liszt)
        print(f"Amount to pay: {round(house, 2)}")
    elif number > 2:
        for i in range(1, 3):
            while True:
                try:
                    price = float(input("Please enter a price: "))
                except ValueError:
                    print("Error. Enter an integer.")
                    continue
                else:
                    break
            liszt.append(price)
            house = sum(liszt)
        for i in range(3, number+1):
            while True:
                try:
                    price = float(input("Please enter a price: "))
                except ValueError:
                    print("Error. Enter an integer.")
                    continue
                else:
                    break
            price = price*0.75
            liszt.append(price)
            house = sum(liszt)
        print(f"Amount to pay: {round(house, 2)}")
def ex26():
    car_speed = int(input("Enter vehicle speed: "))
    speed_limit_min = 40
    speed_limit_max = 140
    boool = car_speed in range(speed_limit_min, speed_limit_max+1)
    if boool == True:
        print("Valid speed")
    else:
        print("Warning: invalid car speed!")

def ex27():
    while True:
        try:
            facebook = int(input("Enter '0' if you do not have a facebook account, otherwise enter any number: "))
            twitter = int(input("Enter '0' if you do not have a twitter account, otherwise enter any number: "))
            instagram = int(input("Enter '0' if you do not have an instagram account, otherwise enter any number: "))
        except ValueError:
            print("Error. Enter an integer.")
            continue
        else:
            break
    facebook = bool(facebook)
    twitter = bool(twitter)
    instagram = bool(instagram)
    list = [facebook, instagram, twitter]
    if list.count(True) >= 2:
        print("You can be a good influencer!")
    else:  
        print("You cannot be a good influencer!")   

def ex28():
    while True:
        try:
            barcode = int(input("Enter EAN-13 article number: "))
        except ValueError:
            print("Error. Enter an integer.")
            continue
        else:
            break
    barcode = str(barcode)
    if len(barcode) == 13:
        print("Article number is correct.")
        if  barcode[:3] == "590":
            print("Article manufactured in Poland")
        else:
            print("Article is foreign")
    else:
        print("Wrong Barcode")
        ex28()
def ex29():    #CIĘŻKE
    jacket = 40
    underwear = 70
    shoes = 20
    rinse = 15
    spin = 9
    time = 0
#Selection of options
    while True:
        inpt = input("Enter to select for washing: jacket, underwear, shoes: ")
        inpt = inpt.lower()
        if inpt == "jacket":
            time += jacket
            break
        elif inpt == "underwear":
            time += underwear
            break
        elif inpt == "shoes":
            time += shoes
            break
        else:
            print("Typing error. Please try again.")
            continue
#Making the rinse option available
    while True:
        addr = input("Do you want additional rinse? Y/N: ")
        addr = addr.lower()
        if addr == "yes" or addr == "y" or addr == "ye":
            time += rinse
            break
        elif addr == "no" or addr == "n":
            break
        else:
            print("Typing error. Please try again.")
            continue
#Making the spin option available
    while True:
        adds = input("Do you want additional spin? Y/N: ")
        adds = adds.lower()
        if adds == "yes" or adds == "y" or adds == "ye":
            time += spin
            break
        elif adds == "no" or adds == "n":
            break
        else:
            print("Typing error. Please try again.")
            continue

    print(f"Total washing time: {time}")

def ex30():
    time = input("Enter time in a 24h format: ")
    if len(time) == 5:
        number = int(time[0:2])
    elif len(time) == 4:
        number = int(time[0:1])
    match number:
        case 13:
            time = time.replace("13", "1")
            print(f"Time in 12-hour format: {time}pm")
        case 14:
            time = time.replace("14", "2")
            print(f"Time in 12-hour format: {time}pm")
        case 15:
            time = time.replace("15", "3")
            print(f"Time in 12-hour format: {time}pm")
        case 16:
            time = time.replace("16", "4")
            print(f"Time in 12-hour format: {time}pm")
        case 17:
            time = time.replace("17", "5")
            print(f"Time in 12-hour format: {time}pm")
        case 18:
            time = time.replace("18", "6")
            print(f"Time in 12-hour format: {time}pm")
        case 19:
            time = time.replace("19", "7")
            print(f"Time in 12-hour format: {time}pm")
        case 20:
            time = time.replace("20", "18")
            print(f"Time in 12-hour format: {time}pm")
        case 21:
            time = time.replace("21", "9")
            print(f"Time in 12-hour format: {time}pm")
        case 22:
            time = time.replace("22", "10")
            print(f"Time in 12-hour format: {time}pm")
        case 23:
            time = time.replace("23", "11")
            print(f"Time in 12-hour format: {time}pm")
        case 24:
            time = time.replace("24", "0")
            print(f"Time in 12-hour format: {time}am")
        case number if 12 >= number >= 0:
            print(f"Time in 12-hour format: {time}am")
        case _:
            print("There is no such time")

def ex31():
    while True:
        try:
            x = int(input("Enter the 'x' coordinate: "))
            y = int(input("Enter the 'y' coordinate: "))
        except ValueError:
            print("Enter a number")
            continue
        else:
            break
    if x > 0 and y > 0:
        print(f"Point P{x, y} is in the first quadrant of the coordinate system")
    elif x < 0 and y > 0:
        print(f"Point P{x, y} is in the second quadrant of the coordinate system")
    elif x < 0 and y < 0:
        print(f"Point P{x, y} is in the third quadrant of the coordinate system")
    elif x > 0 and y < 0:
        print(f"Point P{x, y} is in the fourth quadrant of the coordinate system")

def ex32():
    cs = input("Are you interested in computer science? (Y/N): ")
    cg = input("Do you like playing computer games? (Y/N): ")
    iga = input("Do you have an Instagram account? (Y/N): ")
    cs = cs.upper()
    cg = cg.upper()
    iga = iga.upper()
    if cs == "Y":
        print("Interested in computer science: Yes")
    else:
        print("Interested in computer science: No")
    if cg == "Y":
        print("Playing computer games: Yes")
    else:
        print("Playing computer games: No")
    if iga == "Y":
        print("Has an Instagram account: Yes")
    else:
        print("Has an Instagram account: No")

def ex33():
    while True:
        try:
            number1 = int(input("Enter a decimal number: "))
        except ValueError:
            print("Enter a number")
            continue
        else:
            break
    number = number1
    liszt = ""
    while number//2 != 0:
        rem = number%2
        number = int(number//2)
        liszt = liszt + f"{rem}"   
    if number//2 == 0:
        liszt = liszt + "1"
        liszt = liszt[::-1]
    print(f"{number1}(10) = {liszt}(2)")

def ex34():
    while True:
        try:
            money = int(input("Enter the amount in PLN: "))
        except ValueError:
            print("Enter a number")
            continue
        else:
            break
    fives = money//5
    twos = (money%5)//2
    two = money%5
    ones = two%2
    print(fives, twos, ones)
    print(f"The amount of PLN {money} in coins: ")
    print(f"5 zł - {fives}")
    print(f"2 zł - {twos}")
    print(f"1 zł - {ones}")
    
def ex35():
    for i in range(1, 31):
        if i%3 != 0 and i%5 != 0:
            print(i)
        if i%3 == 0 and i%5 == 0:
            print("BINGO")
        elif i%3 == 0:
            print("THREE")
        elif i%5 == 0:
            print("FIVE")

def ex36():
    while True:
        try:
            number = int(input("Enter a number to multiply: "))
        except ValueError:
            print("Enter a number")
            continue
        else:
            break
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def ex37():
    for pattern in range(0, 6):
        for stars in range(pattern):
            print("*", end="")
        print("")
    for pattern in range(6, 0, -1):
        for stars in range(pattern):
            print("*", end="")
        print("") 
    
def ex38():
    for i in range(1,10):
        for num in range(i):
            print(i, end="")
        print("")

def ex39():
    rows = int(input("Enter how many rows do you want your rectangle to be: "))
    columns = int(input("Enter how many columns do you want your rectangle to be: "))
    for i in range(rows):
        for j in range(columns):
            if i==0 or i == rows -1 or j == 0 or j == columns -1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def ex40():
    string = input("Enter a set of words: ")
    for letter in string:
        print(letter, end=" ")

def ex41():
    PIN = "0805"
    fails = 0
    for tries in range(3):
        pin = input("Enter the pin code: ")
        pin = str(pin)
        if pin == PIN:
            print("PIN code correct.")
            print("Here is your access to your account")
            break
        else:
            print("PIN code incorrect.")
            fails += 1
            continue
    if fails == 3:
        print("Access denied, your card has been blocked")

def ex42():
    for i in range(6,-1,-3):
        for j in range(1,4):
            print(f' {i+j}',end='')
        print()

def ex43():
    f1 = 0
    f2 = 1
    n = int(input("Enter the number of numbers in fibonacci sequence: "))
    count = 0
    next_number = f2
    while count<=n-1:
        print(f1, end=" ")
        count += 1
        f1, f2 = f2, next_number
        next_number = f1+f2
    print()
ex43()
def ex44():
    quantity = 0
    sum = 0
    while True:
        num = int(input("Enter a number(entering zero ends the sequence): "))
        if num != 0:
            quantity += 1
            sum += num
            continue
        elif num == 0:
            break
    mean = sum/quantity
    print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")

def ex45():
    n = int(input("Enter a number of prime numbers to print out: "))
    for nums in range(2, n+1):
        for num in range(2, n+1):
            if nums%num == 0:
                break
        if nums == num:
            print(nums, end=", ")
ex43()

def ex46():
    for n in range(1,8):
        for i in range(0, 49, 7):
            g = n+i
            g = str(g)
            if len(g) == 1:
                g = f" {g}"
            print(f'{g}', end=" ")
        print()
        
def ex47():
    import random
    nums = [5, 6, 7, 8, 9, 10]
    star = 1
    while star<=20:
        print(random.choice(nums))
        star +=1
