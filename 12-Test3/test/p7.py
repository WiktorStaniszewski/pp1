def f(n):
    sum1 = 0
    for i in str(n):
        if str(n).count(i) > 1:
            sum1 += eval(i)
    return sum1



if __name__ == "__main__":
    print(f(1027))
    print(f(4444))
    print(f(22777))
    print(f(230335))
    print(f(513553007))