arr = [2,5,4,7]

#map(#funkcja, #array)   #ma dwa parametry
x = list(map(lambda x:x**2, arr))
print(x)
y = list(filter(lambda x:x%2==1, arr))
print(y)
import functools