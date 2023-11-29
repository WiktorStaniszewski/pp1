with open("powernumbers.txt",'w') as kfc:
    for i in range(1, 11):
        kfc.write(f"{i}"+", "+f"{i**2}"+", "+f"{i**3}"+""+"\n")
    