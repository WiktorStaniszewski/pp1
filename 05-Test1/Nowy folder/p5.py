def f(a, b):
    word = ""
    if a>b:
        for i in range(int(a), int(b)-1, -1):
            if i == b:
                word += str(i)
            else:
                word+=str(i)+","
    return word
