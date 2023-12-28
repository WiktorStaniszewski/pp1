arr = [x for x in range(1,21)]
result = list(filter(lambda x: x%2==0 and x%3==0, arr))
print(result)