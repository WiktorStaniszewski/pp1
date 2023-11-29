count = 0
while True:
    try:
        x = input("Enter the name of the file(without .txt): ")
        with open(f"{x}.txt") as f:
            for i in f.readlines():
                count+=1
        print(f"File name: {x}.txt")
        print(f"Number of lines in a document: {count}")
        break
    except FileNotFoundError:
        print(f"File {x}.txt not found.")
        continue



