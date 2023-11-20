arr = [12, 6, 4, 9, 10]
count = 0
for i in arr:
    if len(str(i)) == 1:
        print(f" {i}: ", end="")
    else:
        print(f"{i}: ", end="")
    print("*"*arr[count])
    count +=1
