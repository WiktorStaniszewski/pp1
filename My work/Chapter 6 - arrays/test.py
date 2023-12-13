def f(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    print(f(1))
    print(f(7))
    print(f(30))
    print(f(2))
    print(f(3))
    print(f(37))
    print(f(38))