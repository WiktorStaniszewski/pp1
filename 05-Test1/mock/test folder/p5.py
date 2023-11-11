'''
The binary system uses two symbols to represent a number: 0 and 1. 
Define a function f(binary_number) that returns True if the given notation is a valid binary number, or false otherwise. 

Example:
f("101101") returns True
f("1311a10100") returns False
'''

def f(binary_number):
    bin = ["0", "1"]
    count = 0
    for i in binary_number:
        if i not in bin:
            return False
        else: 
            count+=1
            continue
    return True