file = open("shopping.txt",'w')
read_product = True
counter = 0
while read_product:
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(f"{counter}. "+product+'\n')
    else:
        read_product = False
file.close()
file = open("shopping.txt", 'r')
file_content = file.read()
file.close()
print(file_content)


'''
wyrażenia regularne - na pewno bedzie na kolosie

'''
