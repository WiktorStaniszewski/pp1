def f(x,y,d):
    nums = [x for x in range(x,y)]
    for i in nums:
        if str(i).__contains__(d):
            return True
    return False

print(f(10,15,"14"))
print(f(100,120,"11"))
print(f(205,210,"04"))
