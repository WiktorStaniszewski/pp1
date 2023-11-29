with open("sample1.txt") as f:
    for line in f:
        print(line, end="")


with open(r"sample2.txt", 'r') as f:
    lines = (f.readlines())
    enumerate(f.readlines())
    print()
    print(len(lines))