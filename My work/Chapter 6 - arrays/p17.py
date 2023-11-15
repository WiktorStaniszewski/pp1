array = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for rows in range(len(array)):
    array[rows][rows]+=1
    print(*array[rows], end=" ")
