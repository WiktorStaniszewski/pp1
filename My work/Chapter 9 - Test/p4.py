def f(arr):
    count = 0
    for i in arr:
        if list(arr).count(i) == 1:
            count += 1
    return count



if __name__ == "__main__":
    print(f([11,22,11,11,22,45,27,11,22,14,14,45]))