def checker(n, n1, n2):
    if int(n) in range(int(n1), int(n2)):
        print(f"Number {n} in the range({n1}, {n2}): yes")
    if int(n) not in range(int(n1), int(n2)):
        print(f"Number {n} in the range({n1}, {n2}): no")