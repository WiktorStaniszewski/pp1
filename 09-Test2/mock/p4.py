def f(subjects):
    sum = 0
    count = 0
    ovcount = 0
    average1 = 0
    subject1 = ''
    average2 = 0
    subject2 = ''
    for key,value in subjects.items():
        ovcount += 1
        for i in value:
            count += 1
            sum += i
        average1 = sum/count
        round(average1, 2)
        sum = 0
        subject1 = key
        if ovcount == 1:
            average2 = average1
            subject2 = subject1
        elif average1>average2:
            average2 = average1
            subject2 = subject1
        count = 0
    return subject2
        
if __name__ == "__main__":
    print(f(({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) ))