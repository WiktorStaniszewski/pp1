array = [[True,False],[True,True],[False,False]]
for row in array:
    for value in row:
        if value == True:
            array[row.index(array)][value.index(array)] = False
        elif value == False:
            value = True
print(array)