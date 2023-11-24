file = open('numbers.txt', 'r')
sum = 0
print("Numbers:", end=" ")
for line in file:
    line = int(line)
    print(line, end=" ")
    sum += line
print()
print(f"Sum: {sum}")
file.close()