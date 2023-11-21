def lenword(word):
    count = 1
    for n in word:
        if n == " ":
            count+=1 
    return count
word = "An apple a day keeps the doctor away"

def orderedwordfl(word):
    array = []
    array = str(word).split()
    array.sort(key=len)
    array.reverse()
    return array

