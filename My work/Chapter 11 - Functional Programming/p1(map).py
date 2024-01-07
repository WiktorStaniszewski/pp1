arr = [2,5,4,7]

#map(#funkcja, #array)   #ma dwa parametry
x = list(map(lambda x:x**2, arr))
print(x)
y = list(filter(lambda x:x%2==1, arr))
print(y)
import functools

def between(a,b):
    list1 = []
    for i in range(a,b+1):
        list(list1).append()
    return list1

between(1,4)