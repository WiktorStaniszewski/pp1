def f(arr):
    for i in arr:
        counti = arr.count(i)
        if counti == 1:
            return i
        else:
            continue



if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))