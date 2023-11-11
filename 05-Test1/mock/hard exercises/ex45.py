def prime(n):
    i = 2
    output = ""
    for num in range(2, i+1):
        for n in range(2, num+1):
            if num%n == 0:
                output += f" {num}"
                output = output.strip()
                i+=1
                break
            elif num%n != 0:
                continue
    return output
print(prime(5))