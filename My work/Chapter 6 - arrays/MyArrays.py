def second_largest(array):
    for i in list(array):
        if i == list(array)[0]:
            larg = i
        else:
            if i > larg:
                secondlarg = larg
                larg = i
    return secondlarg

def difference(array):
    for i in array:
        if i == array[0]:
            minn = i
            maxx = i
        else:
            if i < minn:
                minn = i
            elif i > maxx:
                maxx = i
    return maxx-minn

def median(array):
    array = sorted(list(array))
    num = len(list(array))
    med = list(array)[num//2]
    return med

def largandsmall(array):
    for i in array:
        if i == array[0]:
            minn = i
            maxx = i
        else:
            if i < minn:
                minn = i
            elif i > maxx:
                maxx = i
    arlay = []
    arlay.append(minn)
    arlay.append(maxx)
    return arlay

def minusarray(array):
    word = ""
    count = 0
    for i in list(array):
        count+=1
        if count == len(list(array)):
            word += str(i)
        else:
            word += str(i) + "-"
    return word

