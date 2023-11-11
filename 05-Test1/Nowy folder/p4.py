def f(n):
    output = ""
    count = 0
    if len(str(n)) == 1:
        return f"{n}"
    else:
        for i in str(n):
            count+=1
            if count == len(str(n)):
                output += str(i)
            else:
                if int(i)%2 == 0:
                    output += str(i) + "++"
                elif int(i)%2 != 0:
                    output += str(i) + "+"
    return output

print(f(998877669329382))