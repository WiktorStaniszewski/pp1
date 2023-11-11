def card_number(number):
    print(number[0:2], end="")
    for i in number[2:12]:
        print("*", end="")
    print(number[12:16])