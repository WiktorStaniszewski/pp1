def f(n):
    n1 = 0
    n2 = 1
    next_number = n2
    count = 0
    if n == 1:
        return 0
    while count < n-2:
        next_number = n1+n2
        n1, n2 = n2, next_number
        count +=1
    return next_number

