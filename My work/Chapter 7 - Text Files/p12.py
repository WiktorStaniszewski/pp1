name = "Wiktor Staniszewski"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open('students.txt', 'w')
file.write(name+"\n"+university+"\n"+field)
file.close()
file = open('students.txt', 'r')
file_content = file.read()
file.close()
print(file_content)

