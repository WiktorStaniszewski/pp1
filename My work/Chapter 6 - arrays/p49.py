arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
which_list = 0
counti = 0

for subarr in arr:
    for i in subarr:
        subarr[counti] = 1*(counti+1)
        counti+=1
    counti = 0
counti = 0
for n in arr:
    if which_list != len(arr):
        for i in n:
            if counti != len(n)-1:
                arr[which_list][counti] = i*(which_list+1)
                counti+=1            
            else:
                arr[which_list][counti] = i*(which_list+1)
                counti = 0
                which_list+=1
                break
    else:         
        which_list = 0
        break
for usb in arr:
    for i in usb:
        if len(str(i)) == 1:
            print(f" {i}",end=" ")
        else:
            print(f"{i}",end=" ")
    print()