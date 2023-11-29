with open("sample2.txt", 'r') as f, open("copy2.txt", 'w') as sf:
    for line in f:
        sf.write(line)