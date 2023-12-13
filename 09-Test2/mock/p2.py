def f(arr):
    for i in arr:
        counti = arr.count(i)
        if counti == 1:
            return i



if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([25,25,23]))
    print(f([6,6,6,6,6,6,6,6,6,6,6,6,66]))
    print(f([2,7,7,7,7,7,7,7]))