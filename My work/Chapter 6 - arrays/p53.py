def matrix(dim):
    subarr = [0 for i in range(dim)]
    arr = []
    arr.extend((subarr).copy() for i in range(dim))
    count_array = 0
    count_subarray = 0

    for sa in arr:
        for i in sa:
            if count_subarray == count_array:
                arr[count_array][count_subarray] = 1
            else:
                arr[count_array][count_subarray] = 0
            count_subarray+=1
        count_subarray = 0
        count_array += 1
    
    return arr


for i in matrix(3):
    print(i)