def f(cards):
    sum1 = 0
    for i in cards:
        if i == "A" or i == "K" or i == "Q" or i == "J" or i == "T":
            sum1 += 10
        else:
            sum1 += int(i)
    return sum1



if __name__ == "__main__":
    print(f("234AJ7"))