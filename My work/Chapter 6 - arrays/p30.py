array = [6, 3, 2, 5, 8, 1, 45, 34, 10]
def bubblesort(array):
    if type(array[0]) == int:
        x = sorted(list(array))
        return x
    else:
        return False
print(bubblesort(array))