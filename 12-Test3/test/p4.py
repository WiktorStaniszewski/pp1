def f(addr):
    import re
    words = rf"\b[a-zA-Z]+"
    numbers = rf"[0-9]+"
    gwords = re.findall(words, addr)
    gnums = re.findall(numbers, addr)
    correct = 0
    if len(gnums) == 0 or len(gwords) == 0:
        return False
    else:
        for i in gwords:
            if 1 <= len(i) <= 2:
                correct+=1
        for i in gnums:
            if 1 <= len(i) <= 4:
                correct += 1
        if correct == 2:
            return True
        else: 
            return False



if __name__ == "__main__":
    print(f("A4"))
    print(f("a4"))
    print(f("4a"))
    print(f("bC123"))
    print(f("bcd555"))
    print(f("ss9915"))