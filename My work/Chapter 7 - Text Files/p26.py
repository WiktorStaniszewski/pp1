import re
text = "To be, or not to be, that is the question"
all_words = 0
vowels = re.findall("[qwrtupsdfghjklzxcvbnm]", text, re.IGNORECASE)
all_words = len(vowels)
print(vowels)
print(all_words)