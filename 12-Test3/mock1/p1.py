def f(word):
    count = 0
    result = ''
    for i in range(len(word)):
        if count == len(word)-1:
            
            result += word
        else:
            result += f"{word}-"
            count+=1
    return result

if __name__ == "__main__":
    print(f("book"))
    print(f("water"))
    print(f("ok"))
    print(f("a"))
    print(f(""))