arr = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [8, 7, 6, 5, 4]]
for i in arr:
    print(i)
print(">>>>")
last_arr = []
first_arr = []
count = 0
count_arr = 0
for sa in arr:
    if count == 0:
        first_arr = sa  
        count+=1
    elif count == len(arr)-1:
        last_arr = sa
    else:
        count+=1
        continue

arr[0] = last_arr
arr[-1] = first_arr
for i in arr:
    print(i)