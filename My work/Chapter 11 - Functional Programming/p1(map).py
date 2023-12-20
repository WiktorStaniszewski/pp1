arr = [2,5,4,7]

#map(#funkcja, #array)   #ma dwa parametry
x = sum(list(map(lambda x:x**2, arr)))
print(x)