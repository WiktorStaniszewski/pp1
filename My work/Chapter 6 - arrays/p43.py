sentence = "An apple a day keeps the doctor away"
from MyText import lenword as lw
from MyText import orderedlistalph as ola
from MyText import orderedwordfl as  owf
print(f"Text: {sentence}")
print(f"Number of words: {lw(sentence)}")
print(f"From the longest: {owf(sentence)}")
print(f"Alphabetically: {ola(sentence)}")
