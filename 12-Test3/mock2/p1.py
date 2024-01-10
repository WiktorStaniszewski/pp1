def f(n):
    e = list(str(n))
    an = [eval(i) for i in e]
    an.sort()
    max1 = 0
    min1 = 0
    for i in reversed(an):
        if i%2!=0:
            max1=i
            break
    for i in an:
        if i%2!=0:
            min1=i
            break        
    if min1 == 0 and max1 == 0:
        return -1
    else:
        return(max1-min1)

print(f(10852)) 
print(f(7235973))
print(f(4388))
print(f(846206))

        