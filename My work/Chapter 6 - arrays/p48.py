def create_2d_arr(y,x):
    element = ["0 "*x]
    array = [element*y]
    count = 0
    for i in array:
        for n in i:
            count+=1
            if count == x:
                print(n)
                continue
            else:
                print(n)

create_2d_arr(3, 5)
