import keyboard
count = 0

with open("sample2.txt") as f:
    for i in f.readlines():
        if count != 5:
            print(i)
            count+=1
        elif count == 5:    
            print("Press 'Enter' to continue: ")
            keyboard.wait('enter')
            print()
            
            count=0

