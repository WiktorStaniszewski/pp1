def f(t):
    import re
    pattern = f"\d+"
    x = re.findall(pattern, t)
    sum1 = 0
    for i in x:
        sum1 += int(i) 
    return sum1


if __name__ == "__main__":
    print(f("Water12, and 3play is not 120"))