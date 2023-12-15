def f(d, v):
    count = 0
    for key, value in dict(d).items():
        if value != bool(v):
            count +=1 
    return count


if __name__ == "__main__":
    print(f({"a":False,"b":False,"c":False,"d":True,"e":False}, True))