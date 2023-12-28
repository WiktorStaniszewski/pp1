import statistics
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

mean = round(statistics.mean(list(filter(lambda x:x>2.0,grades))), 2)
print(mean)