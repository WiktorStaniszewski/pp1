stock = [(20,5.5),(15,8.3),(37,3.85),(4,11.6)]
total_value = map(lambda x:x[0]*x[1] ,stock)
print(round(sum(total_value),2))