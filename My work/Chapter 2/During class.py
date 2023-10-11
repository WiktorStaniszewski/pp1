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
ex15()

