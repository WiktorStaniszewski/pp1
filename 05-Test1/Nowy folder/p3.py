def f(n):
    sum = 0
    for i in str(n):
        x = str(n).count(i)
        if int(x)>1:
            sum += int(i)
        else:
            continue
    return sum