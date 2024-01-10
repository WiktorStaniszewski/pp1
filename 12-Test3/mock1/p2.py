def f(x, y, digit):
    result = 0
    for i in range(x,y+1):
        result += str(i).count(str(digit))
    return result

if __name__ == "__main__":
    print(f(10,15,1))
    print(f(28,32,2))
    print(f(100,105,6))
    print(f(100,101,0))
