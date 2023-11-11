'''
A text contains any number of words. 
Define a function f(name) that returns the acronym (first letters of all words). 

Sample result:
f("Internet of Things") returns "IoT"
f("For Your Information") returns "FYI"
f("Python") returns "P"
'''

def f(name):
    nam = ""
    for i in str(name).split():
        nam += i[0]
    return nam
        