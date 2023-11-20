arr = [-15, 8, -31, 47, -2, 19]
for i in arr:
    if i == arr[0]:
        minn = i
        maxx = i
    else:
        if i < minn:
            minn = i
        elif i > maxx:
            maxx = i
print(f"The minimum number is: {minn} and the maximum number is: {maxx}")
