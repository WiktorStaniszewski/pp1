import random
with open("randomnumbers.txt",'w') as kfc:
    for i in range(10):
        kfc.write(str(random.randint(100,999))+"\n")
    