#exercise 6

#a - int
#b - float
#c - int
#d - float
#e - str
#f - bool
#g - bool

#exercise 7



#exercise 8
def ex8():
    number1 = int(input("Type in a number: "))
    number2 = int(input("Type in another number: "))
    result = number1 + number2
    print("The summation of those numbers is: ", result)

#exercise 9
def ex9():
    n1 = 5
    n2 = 1
    n3 = 8
    n4 = 6
    n5 = 3
    sum = n1+n2+n3+n4+n5
    print(sum)
    sq = (((n1)**2)+((n2)**2)+((n3)**2)+((n4)**2)+((n5)**2))
    print(sq)
    quo = n3/n5
    print(quo)
    print(n3==n4)

#exercise 10
def ex10():
    name = input("Type in your name: ")
    age = input("Input your age: ")
    height = input("Type in your height: ")
    print(f"My name is {name}, I am {age} years old, and my height is {height}cm. In 6 years I will be {int(age)+6} years old")

#exercise 11
def ex11():
    fincome = input("Enter father’s income: ")
    mincome = input("Enter mother’s income: ")
    people = int(input("Enter number of people in family: "))
    Total_income = int(fincome) + int(mincome)
    Income_per_person  = Total_income/people
    print(Income_per_person)

#exercise 12
def ex12():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last surname: ')
    full_name = first_name + ' ' + last_name
    print(f'Your fullname is {full_name}')

#exercise 13
def ex13():
    side = int(input("Enter cube side: "))
    print(f"The surface area of a cube with side {side} is {side**2}")

#exercise 14
def ex14():
    pi = 3.14
    r = 5
    area = pi*(r**2)
    circumference = 2*pi*r
    print(f"Area of the circle is {area}")
    print(f"The circumference of the circle is {circumference}")


#exercise 15
def ex15():
    tempC = input("Type in the temperature in Celsius: ")
    try:
        tempF = float(tempC)*1.8000 + 32.00
        tempK = float(tempC) + 273.15
    except ValueError:
        tempC = input("Type in the temperature in Celsius but with a dot: ")
        tempF = float(tempC)*1.8000 + 32.00
        tempK = float(tempC) + 273.15
    print(f"The temperature is {tempC}*C or {tempF}*F or {tempK}*K")

#exercise 16

#exercise 17

#exercise 18
def ex18():
    x = 7
    y = 34
    print("The value of x is: ",x)
    print("The value of y is: ",y)

    x,y = y,x
    print("The values of variables have been swapped")
    print("The value of x is: ",x)
    print("The value of y is: ",y)

#or
def ex181():
    x = 7
    y = 34
    temp = x
    x=y
    y=temp
    print(x, y)

#exercise 19
def ex19():
    a = float(input("The length of a cube's side: "))
    cubeV = a**3
    cubeSA = 6*a**2
    print(f"The volume of said cube is: {cubeV}")
    print(f"The surface area of said cube is: {cubeSA}")

#exercise 20
def ex20():
    a = int(input("Type in the first number: "))
    b = int(input("Type in the second number: "))
    print("The result of division of these numbers, rounded up is: ", round(a/b))
    print("The remainder of the division is: ", a%b)

#exercise 21
def ex21():
    heightcm = input("Type in your height in cm(for feet measurements skip this step): ")
    if heightcm == "":
        heightft = float(input("Type in your height in feet: "))
        convcm = heightft*30.48
        print(f"Your height is {heightft}feet or {round(convcm, 2)}cm")
    else:
        if heightcm == "":
            print(f"Your height is {heightft}feet or {heightft*30.48}cm")
        else:
            convft = float(heightcm)*0.032808
            print(f"Your height is {float(heightcm)}cm or {round(convft, 2)}feet`")

#exercise 22
def ex22():
    a = 3
    b = 5
    c = -2
    print(a - b == -2)

#exercise 23
def ex23():
    import math
    try: a = float(input("Type in the length of the first side: "))
    except ValueError:
        a = float(input("Please input a number: "))
    b = float(input("Type in the length of the second side: "))
    c = float(input("Type in the length of the third side: "))
    s = float((a+b+c)/2)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #according to the heron formula
    circumference = a + b + c
    print(f"The area of the Triangle is {area}")
    print(f"The circumference of the Triangle is {circumference}")

#exercise 24
def ex24():
    reg_number = input("Register you registration number: ")
    if reg_number.__contains__("KR" or "KK"):
        print("This car is from Cracow i.e. True")
    else:
        print("This car is not from Cracow i.e. False")

#exercise 25
def ex25():
    while True:
        try: 
            age = int(input("Please type your age to see if you qualify for exemption: "))
        except ValueError:
            print("Please try again")
            continue
        else:
            break
    if age <= 26:
        print("You are exempt from paying taxes")
    elif 100 > age > 26:
        print("You have to pay taxes")
    elif 0 > age or age >= 100:
        print("You will live forever")

#exercise 26
def ex26():
    while True:
        try:    
            number = int(input("Type in a number: "))
        except ValueError:
            print("Try again")
            continue
        else:
            break
    if number%2 == 0:
        print("Number is even.")
    else:
        print("This number is not even.")

#exercise 27
def ex27():
    while True:
        try:
            num = int(input("Type in a number: "))
        except ValueError:
            print("Type again")
            continue
        else:
            break
    if num in range(-10, 10):
        print(f"True, the number {num} is in the range (-10, 10)")
    else:
        print(f"False, the number {num} is not in the range (-10, 10)")

#exercise 28
def ex28():
    while True:
        try:
            height = float(input("Enter your height: "))
            weight = float(input("Enter your weight: "))
        except ValueError:
            print("Enter again")
            continue
        else:
            break
    height = height/100
    bmi = weight/height**2
    print(f"Your bmi index is: {round(bmi, 2)}")
    match bmi:
        case bmi if bmi <= 18.4:
            print("You're underweight")
        case bmi if 18.4 < bmi <= 24.9:
            print("Your bmi is normal")
        case bmi if 24.9 < bmi <= 39.9:
            print("You're overweight")
        case bmi if 40 <= bmi:
            print("You're morbidly obese")

#exercise 29
def ex29():
    import random
    diceroll = [1, 2, 3]
    first = (random.choice(diceroll))
    second = (random.choice(diceroll))
    third = (random.choice(diceroll))
    print(f"The result of the three dice rolls are: {first}, {second}, {third}")
    result = first + second + third
    print(f"The sum of three dice rolls is {result}")

#exercise 30
def ex30():
    import random
    diceroll = [1, 2, 3, 4, 5, 6]
    rand = random.choice(diceroll)
    print(f"The random dice number is: {rand}")
    print(f"Special number: {rand == 1 or rand == 6}")

#exercise 31
def ex31():
    import random
    diceroll = [1, 2, 3, 4, 5, 6]
    rand = random.choice(diceroll)
    while True:
        try:
            x = int(input("Guess the number on the dice (1-6): "))
        except ValueError:
            print("This is not an integer! Enter again.")
            continue
        else: 
            break
    print(f"The random number is: {rand}")
    if x == rand:
        print("True, you guessed it!")
    else:
        print("False, you didn't get it:c")

#exercise 32
def ex32():
    expense = float(input("Enter a netto value of an object: "))
    VAT = expense*0.23
    expense = round(expense, 3)
    VAT = round(VAT, 2)
    print(f"Ammount: {expense}")
    print(f"VAT 23%: {VAT}")

#exercise 33
def ex33():
    while True:
        password = input("Register your password (at least 8 words): ")
        letters = len(password)
        if letters >= 8:
            print("Valid password")
            break
        else:
            print("Password is invalid")
            continue
#exercise 34
def ex34():
    speed = int(input("Enter vehicle speed: "))
    boool = speed in range(40, 141)
    if boool == True:
        print(f"Speed is valid: {boool}")
    else:
        print(f"Speed is valid: {boool}")

#exercise 35
def ex35():
    while True:
        try:
            circ = float(input("Enter tree circumference: "))
        except ValueError:
            print("Enter a number,", end=" ")
            continue
        else:
            break
    #diameter = 2*radius
    diameter = circ/2
    tbcd = diameter >= 50
    print(f"The diameter of the tree is {diameter}")
    print(f"Tree can be cut down: {tbcd}")

#exercise 36
def ex36():
    bsells = float(input("Enter the bank's sell rates: "))
    bbuys = float(input("Enter the bank's buy rate: "))
    spread = abs(bsells-bbuys)
    bsells = round(bsells, 4)
    bbuys = round(bbuys, 4)
    spread = round(spread, 4)
    print(f"Bank buys EUR for: {bbuys}")
    print(f"Bank sells EUR for: {bsells}")
    print(f"Spread equals: {spread}")

#exercise 37
def ex37():
    personal_data = "Mr. John May, born on 1998-02-16"
    desc = personal_data[4:12]
    name = personal_data[4:8]
    surname = personal_data[9:12]
    ninitial = name[0]
    sinitial = surname[0]
    initials = ninitial+sinitial
    born = personal_data[-10:]
    print(f"Description: {personal_data}")
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Initials: {initials}")
    print(f"Born: {born}")

#exercise 38
def ex38():
    while True:
        try:
            phnumber = input("Enter a phone number: ")
        except ValueError:
            print("Type an integer")
            continue
        else:
            break
    phnumber = "-".join(phnumber[i:i+3] for i in range(0, len(phnumber), 3))
    print(phnumber)

#exercise 39
def ex39():
    while True:
        try:
            price = float(input("Enter the price of a product: "))
            discount = int(input("Enter the value of the discount: "))
        except ValueError:
            print("Enter a digit")
            continue
        else:
            break
    discount = 1 - discount/100 
    pwd = price*discount
    reduction = price - pwd
    print(f"Price with a discount: {round(pwd, 2)}")
    print(f"Reduction: {round(reduction, 2)}")

#exercise 40
def ex40():
    while True:
        try:
            ccnumber = int(input("Enter the credit card number: "))
        except ValueError:
            print("We only accept digits")
            continue
        if len(str(ccnumber)) != 16:
            print("Enter a correct number of digits")
            continue
        else: 
            break
    ccnumber = str(ccnumber)
    ccnumber = " ".join(ccnumber[i:i+4] for i in range(0, len(str(ccnumber)), 4))
    print(f"Credit card number: {ccnumber}")

#exercise 41
def ex41():
    while True:
        try:
            num = int(input("Enter a number for conversion: "))
        except ValueError:
            print("Enter a digit")
            continue
        else:
            break
    binary = bin(num)
    hexadecimal = hex(num)
    print(f"Binary number: {binary}")
    print(f"Hexadecimal number: {hexadecimal}")

#exercise 42
def ex42():
    while True:
        binary = input("Enter a 4-digit binary number: ")
        if len(str(binary)) != 4:
            print("Enter a correct number of digits")
            continue
        else: 
            break
    binary = list(binary)
    binary.reverse()
    if binary[0] == "1":
        first = 2**0
    else:
        first = 0
    if binary[1] == "1":
        second = 2**1
    else:
        second = 0
    if binary[2] == "1":
        third = 2**2
    else:
        third = 0
    if binary[3] == "1":
        fourth = 2**3
    else:
        fourth = 0
    number = first+second+third+fourth
    print(f"Binary number in decimal notation: {number}")         

#exercise 43
def ex43():
    name = input("Type in your name: ")
    name = list(name)
    for letter in name:
        print(f"{letter} ({ord(letter)})")
            