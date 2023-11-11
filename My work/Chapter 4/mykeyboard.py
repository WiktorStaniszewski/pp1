def generate_number():
    import random
    x = range(1,9)
    y = random.choice(x)
    return y
def read_number():
    z = int(input("Enter a one-digit number: "))
    return z