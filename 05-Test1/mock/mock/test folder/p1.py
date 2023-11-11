'''The vending machine accepts 1, 2 and 5 PLN coins. 
Define the function f(amount_to_pay) that returns the minimum 
number of coins that can be used to pay for the purchased product. 

Sample result:
f(23) returns 6
f(8) returns 3
'''
def f(amount_to_pay):
    fives = amount_to_pay//5
    twos = (amount_to_pay%5)//2
    two = (amount_to_pay%5)%2
    ones = two
    return fives + twos + ones