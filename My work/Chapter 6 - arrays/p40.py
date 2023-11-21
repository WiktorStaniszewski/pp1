import random
n = int(input("Enter a number of random numbers: "))
count = 0
def randintnum():
    x = random.randint(1, 999)
    if len(str(x)) == 1:
        return f"   {x}"
    elif len(str(x)) == 2:
        return f"  {x}"
    elif len(str(x)) == 3:
        return f" {x}"
def lines(n):
    print("-"+"-"*5*n, end="")

lines(n)
print()
for i in range(n):
    if count == 0:
        print(f"|{randintnum()}", end="|") 
        count=+1
    else:
        print(f"{randintnum()}", end="|")
        count=+1
print()
lines(n)

