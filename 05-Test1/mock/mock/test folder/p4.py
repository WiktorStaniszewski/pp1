'''
The credit card number consists of 16 digits. 
Define a function f(card_number) that masks the card number. 
The function returns a character string in which only the first two and the last four digits of the card number are visible. 
The remaining digits of the card number are replaced with an asterisk. 

Sample result:
f("5290312400019022") returns "52**********9022"
'''

def f(card_number):
    cnum = ""
    if len(card_number) != 16:
        return False
    cnum += card_number[0:2]
    for i in card_number[2:12]:
        cnum += "*"
    cnum += card_number[12:16]
    return cnum