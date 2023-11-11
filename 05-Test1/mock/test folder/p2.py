'''Define the function f(n1,n2,n3) 
that returns True if all three numbers 
n1,n2,n3 are different or False otherwise. 

Sample result:
f(4,8,5) returns True
f(2,9,2) returns False
'''

def f(n1, n2, n3):
    liszt = [n1, n2, n3]
    for i in liszt:
        x = liszt.count(i)
        if x>1:
            return False
        else:
            continue
    return True
print(f(7, 5, 5))