with open("sample2.txt", 'r') as f, open("copy.txt", 'w') as sf:
    for line in f:
        sf.write(line)        