def f(fnc, res):
    res.sort()
    result = list(filter(fnc, res))
    max1 = result[-1]
    min1 = result[0]
    return max1 - min1



if __name__ == "__main__":
    res = [95,90,20,50,70]
    fnc1 = lambda x:x>50
    fnc2 = lambda x: x>30 and x<90
    print(f(fnc1, res))
    print(f(fnc2,res))