countries = [
    {"name":"Poland", "Population":39000000},
    {"name":"Ukraine", "Population":44000000},
    {"name":"Slovakia", "Population":5447000},
    {"name":"Germany", "Population":83200000},
    {"name":"France", "Population":67750000}
]
count = 0
print("="*22)
for i in countries:
    for key, value in i.items():
        if count%2==0:
            print("{:<10} | {:<10}".format("Country", value))
        elif count%2==1:
            print("{:<10} | {:<10}\n".format(key, value))
        count+=1
print("="*22)