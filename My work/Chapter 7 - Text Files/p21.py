with open("newnumbers.txt", 'w') as nnf:
    for i in range(1, 51):
        nnf.write(str(i)+"\n")