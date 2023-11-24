def lenword(word):
    count = 1
    for n in word:
        if n == " ":
            count+=1 
    return count


def orderedwordfl(word):
    array = []
    array = str(word).split()
    array.sort(key=len)
    array.reverse()
    arr =""
    count = 0
    for i in array:
        count+=1
        if count == len(array):
            arr+=str(i)
        else:
            arr+=str(i)+","
    return arr

def orderedlistalph(word):
    array=[]
    array = str(word).split()
    array.sort()
    arr =""
    count = 0
    for i in array:
        count+=1
        if count == len(array):
            arr+=str(i)
        else:
            arr+=str(i)+","
    return arr
