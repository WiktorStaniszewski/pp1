arr1 = [5,3,1]
arr2 = [2,3,4,8,4,9,7,5]
countyes = 0
countno = 0
for i in arr1:
    if i in arr2:
        countyes+=1
        print("+")
        if countyes == len(arr1):
            print("Array 1 is a subset of array 2")
            break
    else:
        countno += 1
        print("-")
        if countno > 0:
            print("Array 1 is not a subset of array 2")
            break