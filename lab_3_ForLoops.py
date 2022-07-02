def q1():
    for i in range(1, 16):
        print(i)


def q2():
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)


def q3():
    print("This are the even numbers: ")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)


def q4():
    odd_numbers = []
    even_numbers = []
    for i in range(1, 21):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    print(f"These are odd numbers:\n", *odd_numbers)
    print(f'These are even numbers: \n', *even_numbers)


def q5():
    number = int(input("Enter a number: "))

    for i in range(1, 11):
        times_number = number * i
        print(f'{number} x {i} = {times_number}')


def q6():
    evensum = 0
    oddsum = 0
    for i in range(1, 11):
        if i % 2 == 0:
            evensum += i
        else:
            oddsum += i
    print(f'ODDSUMS: {oddsum}')
    print(f'EVENSUMS: {evensum}')


def q7():
    num = int(input("Enter a number: "))

    for i in range(num-1, 1, -1):
        num *= i

    print(f'The factorial is {num}')


def q8():
    num = input("Enter a number: ")

    rev_num = ''
    for i in range(len(num), 0, -1):
        rev_num += num[i-1]

    print(f"This is the reversed number: {rev_num}")


def q9():
    number = input("Enter few digits: ")

    order = len(number)
    sum = 0
    for i in number:
        sum += int(i) ** order

    if number == str(sum):
        print(number, ". This is an ARMSTRONG number")
    else:
        print("This is not an ARMSTRONG number")


def q10():
    num = input("Enter a few digits: ")
    rev_num = ''
    for i in reversed(num):
        rev_num += i

    if rev_num == num:
        print("This is a Palindrome number")
    else:
        print("This is not a Palindrome number")


def q11():
    t1 = 0
    t2 = 1
    nterms = int(input("Enter a number of terms: "))
    print(f"Fibonacci sequence up to {nterms}: ")
    for i in range(1, nterms + 1):
        print(t1)
        next_term = t1 + t2
        t1 = t2
        t2 = next_term


def q12():
    num = input("Enter a digit: ")
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)


def q13():
    num = int(input("Enter a number: "))

    for i in range(2, num + 1):
        if num % i == 0:
            print("This is not a prime number")
            break
        else:
            print("This is prime number")
            break


def q14():
    for i in range(100, 1000):
        sum = 0
        for x in str(i):
            sum += int(x) ** 3

        if sum == i:
            print(i)


q14()


def q15():
    number = input("Enter few digits: ")

    order = len(number)
    sum = 0
    for i in number:
        sum += int(i) ** order

    if number == str(sum):
        print(number, ". This is an ARMSTRONG number")
    else:
        print("This is not an ARMSTRONG number")


def q16():
    for i in range(1, 201):
        strnum = str(i)
        if ("".join(reversed(strnum)) == strnum):
            print(i)


def q17():
    a = [1]
    numlist = []
    for i in a:
        a.append(i)
        number = int(input("Enter number: "))
        numlist.append(number)
        if number == 0:
            print(max(numlist))
            break


def q18():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    for i in range(1, (num1 + num2)):
        if (num1 % i == 0 and num2 % i == 0):
            val = i
    print(val)


def q19():
    num = int(input("Enter a number: "))

    for i in range(2, num + 1):
        if num % i == 0:
            print("not prime")
            sum = 0
            for x in str(num):
                sum += int(x)
            print(sum)
            break
        else:
            print("prime")
            for y in range(2, num):
                num *= y
            print(num)
            break


def q20():
    number = input("Enter number: ")

    order = len(number)
    sum = 0
    for i in number:
        sum += int(i) ** order

    if number == str(sum):
        print("Armstrong")
        rev = ''
        for i in reversed(number):
            rev += i

        print(rev)
    else:
        print("Not Armstrong")
        rev = ''
        for i in reversed(number):
            rev += i

        if rev == number:
            print("This is Palindrome")


def q21():
    number = int(input("Enter numbers: "))

    for i in range(2, number):
        number *= i

    if number >= 500:
        sum = 0
        for x in str(number):
            sum += int(x)
        print(sum)
    else:
        rev_num = ''
        for i in reversed(str(number)):
            rev_num += i
        print(rev_num)
