<<<<<<< HEAD
#Exercise 1
5           #integer
x = 5       #assigns a value to a variable "x", przypisanie
x + 1       #adds one to a variable "x"

#Exercise 2

x = input("Please enter your name: ")
print("Hello " + x)

#Exercise 3

hours = float(input("Please enter you hours: "))
rate = float(input("Enter you rate: "))
print(("Your pay is {}$").format(hours*rate))

#Exercise 4

width = 17
height = 12.0

a = print(width//2)     #  8 - int
b = print(width/2)      #  8.5 - float
c = print(height/3)     #  4.0 - float
print(1+2*5)            #  11 - int

#Exercise 5

tempC = input("Type in the temperature in Celsius: ")
try:
    tempF = float(tempC)*1.8000 + 32.00
except ValueError:
    tempC = input("Type in the temperature in Celsius but with a dot: ")
    tempF = float(tempC)*1.8000 + 32.00
print(("The temperature is {}*C or {}*F").format(tempC, tempF))

=======
#Exercise 1
5           #nothing
x = 5       #assigns a value to a variable "x"
x + 1       #adds one to a variable "x"

#Exercise 2

x = input("Please enter your name: ")
print("Hello " + x)

#Exercise 3

hours = float(input("Please enter you hours: "))
rate = float(input("Enter you rate: "))
print(("Your pay is {}$").format(hours*rate))

#Exercise 4

width = 17
height = 12.0

a = print(width//2)     #  8 - int
b = print(width/2)      #  8.5 - float
c = print(height/3)     #  4.0 - float
print(1+2*5)            #  11 - int

#Exercise 5

tempC = input("Type in the temperature in Celsius: ")
try:
    tempF = float(tempC)*1.8000 + 32.00
except ValueError:
    tempC = input("Type in the temperature in Celsius but with a dot: ")
    tempF = float(tempC)*1.8000 + 32.00
print(("The temperature is {}*C or {}*F").format(tempC, tempF))

>>>>>>> bace6a014cfa3bbb6411c6192cda48c8250e2b6e
