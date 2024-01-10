def f(arr):
    for i in arr:
        counter = arr.count(i)
        if counter == 1:
            return i



if __name__ == "__main__":
    print(f([5,6,6,6]))
    print(f([8,8,8,8,9]))
    print(f([25,25,23]))
    print(f([7,7,7,7,7,5,7,7]))