def f(d):
    people = 0
    count = 0
    avg = 0
    result = 0
    for key,value in d.items():
        people+=value
        count+=1
    avg=people/count
    for key,value in d.items():
        if value>avg:
            result+=1
    return result

print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))
