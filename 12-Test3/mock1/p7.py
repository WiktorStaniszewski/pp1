def f(arr2d):
    count = 0
    result = 0
    allnums = max(len(rows) for rows in arr2d)
    alist = [0 for i in range(allnums)]
    while count !=allnums:
        for i in arr2d:
            if count+1 > len(i) < allnums:
                continue
            else:
                alist[count] += i[count]
        count+=1
    print(alist)
    for repeat in alist:
        if alist.count(repeat) > 1:
            return True
    return False
            



arr = [[8,9,9,9,8,9],
       [2,2,2,0],
       [5,0,0,5],
       [4,7,0,2],
       [0,2,0,0]]
if __name__ == "__main__":
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]]))
    print(f([[3,4],[5,1],[4,7]])) 
    print(f([[3,4],[5,9],[4,7]]))
    print(f(arr))