array1 = [15, 8, 31, 47, 2, 19, 100, 25, 49, 81, 1, 7, 3, 76, 12, 24, 36, 58]

def rand_elem(array):
    import random
    return random.choice(array)

print(rand_elem(array1))
