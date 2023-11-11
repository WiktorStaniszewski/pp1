for i in range(1, 8):
    for x in range(0, 49, 7):
        g = x+i
        if len(str(g)) == 1:
            g = f" {g}"
        print(g, end=" ")
    print()