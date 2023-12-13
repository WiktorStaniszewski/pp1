import stack 
def convert(number):
    import stack
    while number!=0:
        if number%2 != 0:
            stack.push(1)
        else:
            stack.push(0)
        number //= 2        
    stack.display()


convert(18)