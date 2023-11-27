arr = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [8, 7, 6, 5, 4]]
for i in arr:
    print(i)
print(">>>>")
count = 0
count_arr = 0
for sa in arr:
    for i in sa:
        if count == 0:
            first = i
            count+=1
        
        elif count == len(arr[count_arr]):
            last = i
            count = 0
        else: 
            count += 1
    x = arr[count_arr][0]
    arr[count_arr][0] = arr[count_arr][-1]
    arr[count_arr][-1] = x
    
    count_arr +=1
for i in arr:
    print(i)