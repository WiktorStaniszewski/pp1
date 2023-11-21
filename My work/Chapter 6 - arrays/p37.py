from MyArrays import largandsmall as las
from MyArrays import second_largest as sl
from MyArrays import difference as dif
from MyArrays import median as med
from MyArrays import minusarray as ma

arr = [7,3,8,5,2]

print(f"Second largest number: {sl(arr)}")
print(f"Smallest and largest number: {las(arr)}")
print(f"Difference between largest and smallest: {dif(arr)}")
print(f"Median: {med(arr)}")
print(f"Numbers as string: {ma(arr)}")
