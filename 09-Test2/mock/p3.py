def f(array2d):
    count_arrays = 0
    sumrow = 0
    sumcolumn = 0
    
    for arr in array2d:
        for i in arr:
            sumrow += i
        for n in array2d:
            sumcolumn += n[count_arrays]
        count_arrays+=1
        if sumrow == sumcolumn:
            continue
        else:
            return False
    return True



if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))
    
'''
[[3,7,2],
 [4,2,5],
 [5,2,1]]
'''