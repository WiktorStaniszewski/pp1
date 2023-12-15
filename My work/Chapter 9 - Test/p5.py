def f(arr2d):
    count = 0
    for array in arr2d:
        if array[0]**2 == array[1]:
            count+=1
    return count
            




if __name__ == "__main__":
    print(f([[4,16],[3,9],[-3,-9]]))