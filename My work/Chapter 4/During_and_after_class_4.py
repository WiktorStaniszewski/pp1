def ex1():
    #a
    print(len('computer science'))
    #b
    x = input("Enter something")
    print(x)
    #c
    y = str(5058)
    print(y, type(y))
    #d
    z = int(20303)
    print(z, type(z))
    #e
    liszt = [4, 7, 2, 3, 9, 8]
    print(min(liszt))

def ex2():
    import math
    #a
    print(math.log(5))
    #b
    print(math.pow(math.e, 3))
    #c
    print(math.sqrt(7))
    #d
    print(math.sin(math.pi/2))

def ex7():
    def bmicalc(weight = 0, height = 0):
        height = height/100
        bmi = weight/height**2
        print("Your BMI is:",bmi)
    bmicalc(weight = 60, height = 184)
#
def ex2_1():
    
    def repeat_lyrics():
        print_lyrics()
        print_lyrics()
    def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')
    repeat_lyrics()
    
def ex4_1():
    #d 
    pass

def ex5_1():
    #d
    pass

def ex6_1():
    def computepay(hours, rate):
        if hours > 40:
            overtime = hours - 40
            pay = 40*rate + overtime*rate*1.5
            print(pay)
        elif hours <= 40:
            pay = hours*rate
            print(pay)
    computepay(45, 10)

def ex7_1():
    def computegrade(score):
        if 1 >= score >= 0.9:
            print("Grade A")
        elif 0.9 > score >= 0.8:
            print("Grade B")
        elif 0.8 > score >= 0.7:
            print("Grade C")
        elif 0.7 > score >= 0.6:
            print("Grade D")
        elif 0 < score < 0.6:
            print("Grade F")
        else:
            print("Bad Score")
    computegrade()

def ex7_2():
    def product(x,y):
        return x*y

    a = 3
    b = 4
    print(f"The product of {a} and {b} is {product(a,b)}")

def ex12():
    liszt = [7, 5, 6, 3, 8, 2]
    print(max(liszt))
    print(min(liszt))
    print(bin(304))
    print(hex(304))
    print(int("€"))
    print(abs(-17))

def ex13():
    import math
    print(math.log(5))
    print(math.pow(math.e, 3))
    print(math.sqrt(7))
    #rad =
     
def ex14():
    def display_program_name():
        print('Informatyka Stosowana')
    count = 1
    while count <=4:
        display_program_name()
        count+=1


#ex15
def phone_keyboard():
    for i in range(1, 8, 3):
        for num in range(0, 3):
            print(i+num, end=" ")
        print()

def ex16():
    def calc(x, y):
        return x*y
    a = 4
    b = 2
    print(f"The product of {a} and {b} is {calc(a, b)}")

def ex17():
    def difference():
        if n1 == n2 == n3:
            return f"All numbers: {n1}, {n2}, {n3} are equal"
        else:
            if n1 == n2:
                return f"The first number: {n1} and the second: {n2} are the same"
            elif n2 == n3:
                return f"The second number: {n2} and the third: {n3} are the same"
            elif n1 == n3:
                return f"The first number: {n1} and the third: {n3} are the same"
            else:
                return f"All numbers: {n1}, {n2}, {n3} are different"
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    print(difference())
def ex18():
    def numbers(n):
        n+=1
        text = ""
        for number in range(1, n):
            number = str(number)
            text += number + " "
        return text
    n = int(input("Enter the amount of numbers to print: "))
    print(numbers(n))
#def ex19():
    

def ex21():
    from mykeyboard import generate_number, read_number
    y = generate_number()
    z = read_number()
    if y == z:
        print(f"Your number: {z}")
        print(f"Computer number: {y}")
        print("You won the Game")
    else:
        print(f"Your number: {z}")
        print(f"Computer number: {y}")
        print("You lost the Game")

def ex22():
    from calendar import month 
    n = int(input("Enter the number of the month: "))
    print(f"The name of the month {n} is: {month(n)}")

def ex23():
    from letterss import calc
    sent = input("Enter a phrase or sentence: ")
    x = input("Enter a letter which is to be counted: ")
    print(f"The number of letters '{x}' is: {calc(sent, x)}")

#ex24 in different file

def ex25():
    x = lambda a, b: bool(a>b)
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(x(n1, n2))

def ex26():
    y = lambda a: bool(a%2 == 0)
    n1 = int(input("Enter a number please: "))
    print(y(n1))

#ex27 in a separate module

def ex28():
    bin = input("Enter a binary number: ")
    def binary_num():
        binary = ["0", "1"]
        count = 0
        for i in bin:
            if i not in binary:
                print(f"{bin} is not a binary number")
                return False
            else:
                count += 1
                continue
        print(f"{bin} is a binary number")
    binary_num()


def ex29():
    def amount_to_pay(cost):
        fives = cost//5
        twos = (cost%5)//2
        two = cost%5
        ones = two%2
        return fives + twos + ones
    money = int(input("Enter the amount of money: "))    
    print(f"{money}PLN requires you to give {amount_to_pay(money)} coins")

def ex30():
    def f(number, even):
        sum = 0
        if even == "True":
            for i in number:
                if int(i)%2 == 0:
                    sum += int(i)
        elif even == "False":
            for i in number:
                if int(i)%2 != 0:
                    sum += int(i)
        return sum
    num1 = input("Enter a number: ")
    evenness = input("Even or odd (True or False?): ")
    evenness = evenness.capitalize()
    print(f"f({num1}, {evenness}) returns: {f(num1, evenness)}")

def ex31():
    def f(x, y):
        count = 0
        for i in range(int(x), int(y)):
            if i < 0:
                if i%2 == 0:
                    count += 1
        return count
    num1 = input("Enter the first number of the range: ")
    num2 = input("Enter the second number of the range: ")
    print(f"f({num1}, {num2}) returns {f(num1, num2)}")

def ex32():
    def f(n1, n2, n3):
        if int(n1)<0:
            return True
        else:
            if int(n2)<0:
                return True
            else:
                if int(n3)<0:
                    return True
                else:
                    return False
    x = input("Enter the first number: ")
    y = input("Enter the first number: ")
    z = input("Enter the first number: ")

    print(f"f({x}, {y}, {z}) returns {f(x, y, z)}")

def ex33():
    def f(n):
        nick = ""
        count = 0
        for i in range(int(n)):
            if count < int(i):
                nick = nick + "/"
                nick = nick + "*"
                count += 1
            elif count == int(i):
                nick = nick + "*"        
        return nick
    x = input("Enter the number: ")
    print(f(x))

def ex34():
    def f(n):
        numbers = 0
        num = ""
        for i in range(n):
            numbers = numbers + 1
            num += str(numbers) + " "
        return num
    number = int(input("Enter a number: "))
    print(f"f({number}) returns {f(number)}")    

def ex35():
    def f(n1, n2, op):
        if op == "+":
            return n1+n2
        elif op == "%":
            return n1%n2
        elif op == "**":
            return n1**n2
        elif op == "*":
            return n1*n2
        elif op == "-":
            return n1-n2
        else:
            print("Wrong operator, launch again.")
    print("A function asks for a number, a second number and an operator, (+, %, **, *, -)")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Enter the operator: ")
    print(f"The function f({num1}, {num2}, '{op}') returns {f(num1, num2, op)}")

def ex36():
    def detector(n):
        patst = 0
        for i in n:
            if i == "+":
                patst += 1
            elif i == "-":
                patst -= 1
            if patst == 3:
                return "True"
        return "False"
    detect = input("Enter a '+' if anyone enters and a '-' if anyone leaves: ")
    print(f"The function f('{detect}') returns {detector(detect)}")

def ex37():
    def fibonacci(n):
        n1 = 0
        n2 = 1
        count = 0
        nn = n2
        while count <= n-2:
            count += 1
            n1, n2 = n2, nn
            nn = n2+n1
        return n1
    print(fibonacci(100))

def ex38():
    def palindrome(exp):
        rev = exp[::-1]
        if rev == exp:
            return True
        else:
            return False
    typo = input("Enter a palindrome word: ")
    print(f"A word '{typo}' as a palindrome word returns {palindrome(typo)}")

def ex39():
    def space_removal(sentence):
        sent=""
        for i in sentence:
            if i != " ":
                sent += i
            elif i == " ":
                i = str(i).replace(" ", "")
                sent +=i
        return sent

    print(space_removal("A programming language is a system of notation for writing computer programs"))

def ex40():
    def f(num):
        sum = 0
        for i in str(num):
            number = str(num).count(i)
            if number > 1:
                sum += int(i)
        return sum
    print(f(513553007))

def ex41():  #what should i do here?
    def prime(n):
        list = []
        x = 0
        while x>1:
            x+=1
        while len(list)<=n:
            if n == 1:
                return 2
            for n1 in range(2, x):
                for n2 in range(2, x):
                    if n1%n2 == 0:
                        break
                if n1 == n2:
                    list.append(n1)
                    continue
        return list[n-1]
    print(prime(5))
'''
    def f(n):
        result=2
        now=result
        while(n>1):
            now+=1
            is_prime=True
            for x in range(2,now):
                if now%x == 0:
                    is_prime=False
            if is_prime == True:
                result=now
                n-=1
        return result
'''
def ex43():
    def acro(name):
        output = ""
        for i in str(name).split():
            print(i)
            output += i[0]
        return output
    print(acro("Internet of Things"))

def ex44():
    def corrector(password):
        if str(password).__len__() < 6:
            return False
        else:
            for i in password:
                if str(password).count(i) > 1:
                    return False
            return True
    passwoord = input("Please enter your new password: ")
    print(f"Your new password is correct: {corrector(passwoord)}")

def ex45():
    def maths(sub):
        return eval(sub)
    print(maths("9+2+3-1-9"))

def ex41():
    def f(n1, n2, n3):
        list = [int(n1), int(n2), int(n3)]
        list.sort()
        small = list[0]
        largest = list[-1]
        return largest - small
    print(f(2, 12, 8))

def ex46():
    def f(x, y):
        sum = 0
        for i in range(int(x), int(y)+1):
            if i%2 == 0 and i%3 == 0:
                if i%4 == 0:
                    continue
                else: 
                    sum += i
        return sum
    print(f(10, 30))

def ex47():
    def dash(text):
        word =""
        str(text).split()
        for letters in text:
            if letters == text[-1]:
                word+=letters
                break
            letters += "-"
            word += letters
        return word
    print(dash(""))

'''
3 digits + 4th control digit
4th = (n1 + n2 + n3)%7
'''

def ex48():
    def f(product_code):
        sum = 0
        if len(product_code) != 4:
            return False
        for n in str(product_code)[0:3]:
            sum += int(n)
        if sum%7 == int(product_code[-1]):
            return True
        else:
            return False
    print(f("7071"))

'''a number of dice rolls in a row'''
def ex49():
    def f(dice):
        x = int
        count = ""
        nir = []
        counter = 0
        data = ""
        for i in dice:
            if i == x:
                data += f"{i}"
                data = str(count) + f"{i}"
                nir.append(data) #nir => numbers in a row list
                counter = len(data)
                print(counter, data)
            elif i!=x and counter>len(data):
                data=[]
                continue
            x = i
        return max(nir)
    print(f("3089302332333821788"))
def ex491():
    def f(dice):
        if dice == "":
            return None  

        max_roll = None
        max_count = 1
        current_roll = dice[0]
        current_count = 1

        for i in range(1, len(dice)):
            if dice[i] == current_roll:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
                    max_roll = current_roll
            else:
                current_roll = dice[i]
                current_count = 1

        return max_roll

    if __name__ == "__main__":
        dice = "5233165554211"
        max_roll = f(dice)
        print(f"f({dice}) returns {max_roll}")

        dice = "2133"
        max_roll = f(dice)
        print(f"f({dice}) returns {max_roll}")

        dice = "111144444111"
        max_roll = f(dice)
        print(f"f({dice}) returns {max_roll}")

def factorial(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
    
def ex51():
    def sum(n):
        if n==0 or n==1:
            return 1
        if n > 1:
            return n + sum(n-1)
    print(sum(10))

def power(x, n):
    powerade = x*x**(n-1)