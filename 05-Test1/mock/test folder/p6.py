'''
Create a function f(number, even) that computes the sum of the digits of a number. 
When the value of the even parameter is True, the function returns the sum of the even digits. 
When the value of the even parameter is False, the function returns the sum of the odd digits. 

Example:
f(3124,True) returns 6
f(3124,False) returns 4
f(20576,False) returns 12
f(20576,True) returns 8
f(13115,True) returns 0
'''

def f(number, even):
    sum = 0
    if even == True:
        for i in str(number):
            if int(i)%2==0:
                sum += int(i)
        return sum
    elif even == False:
        for i in str(number):
            if int(i)%2!=0:
                sum += int(i)
        return sum