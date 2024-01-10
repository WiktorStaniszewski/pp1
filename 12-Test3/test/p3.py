def f(arr2d):
    first = arr2d[0]
    last = arr2d[-1]
    arr2d[0] = last
    arr2d[-1] = first
    return arr2d

if __name__ == "__main__":
    print(f([[1,2,3,4],[5,6,7,8]]))
    print(f([[1,1],[2,2],[3,3],[4,4]]))