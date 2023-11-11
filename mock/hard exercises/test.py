def calc(cc_number):
    x = " ".join(cc_number[i: i+4] for i in range(0, len(cc_number), 4))
    print(x)

def sdsdsdsds():
    phnumber = "732661292"
    x = "-".join(phnumber[i:i+3] for i in range(0, len(phnumber), 3))
    print(x)

def exexex():
    n = 1 
    while n<=10:
        print(f"1:{n} = {round(1/n, 2)}")
        n+=1

def star(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()
    for x in range(n, 0, -1):
        for y in range(x):
            print("*", end=" ")
        print()
star(10)

def betstar():
    n = 5
    m = n-1
    for row in range(-m, m+1):
        for col in range(-m, m+1):
            if abs(row) + abs(col) == m:
                c = '*'
            else:
                c = ' '
            print(c, end='')
        print()

def number_star():
    for i in range(10):
        for x in range(i):
            print(f"{i}", end="")
        print()

x = "Krakow University of Economics"
print(" ".join(x[i] for i in range(0, len(x))))