def f(sth):
    count = 0
    for i in sth:
        if i == "+":
            count +=1
        elif i == "-":
            count -= 1
    return count


if __name__ == "__main__":
    print(f("+-+++-+---"))