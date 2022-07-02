def q1():
    i = 0
    while (i <= 14):
        i += 1
        print(i)


def q2():
    x = 0
    y = 0
    i = 0

    while i < 10:
        x += 1
        y += x
        i += 1
    print(y)


def q3():
    i = 0
    print("The even numbers: ")
    while i < 20:
        i += 1
        if i % 2 == 0:
            print(i)


def q4():
    even_numbers = []
    odd_numbers = []
    i = 0
    while i < 20:
        i += 1
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    print(odd_numbers)
    print(even_numbers)


def q5():
    number_given = int(input("Enter a number: "))
    i = 1
    while (i <= 10):
        times_number = number_given * i
        print(f'{number_given} x {i} = {times_number}')
        i += 1


def q6():
    oddsum = 0
    evensum = 0

    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            evensum += i
        else:
            oddsum += i
    print(f'ODDSUMS: {oddsum}')
    print(f'EVENSUMS: {evensum}')


def q7():
    number = int(input("Enter a number: "))

    i = number

    product = i
    while (i >= 2):
        product *= (i-1)
        i -= 1

    print(f'The factorial of {number} is {product}')


def q8():
    number = int(input("Enter numbersss: "))
    reversed_number = 0

    while number != 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder

        number //= 10

    print(reversed_number)


def q9():
    number = int(input("Enter few digits: "))

    order = len(str(number))
    sum = 0

    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        print(number, ". This is an ARMSTRONG number")
    else:
        print("This is not an ARMSTRONG number")


def q10():
    number = int(input("Enter a few digits: "))
    num = number
    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder

        number //= 10

    if reversed_number == num:
        print("This number is a Palindrome")
    else:
        print("This number is not a Palindrome")


def q11():
    t1 = 0
    t2 = 1
    count = 0
    nterms = int(input("Enter number of terms: "))

    print(f"Fibonacci sequence up to {nterms}: ")
    while (count < nterms):
        print(t1)
        next_term = t1 + t2
        t1 = t2
        t2 = next_term
        count += 1


def q12():
    num = int(input("Enter number: "))

    sum = 0
    while num > 0:
        remainder = num % 10
        sum += remainder
        num //= 10

    print(sum)


def q13():
    num = int(input("Enter a number: "))

    i = 2
    while i < num:
        if (num % i) == 0:
            print("This is not a prime number")
            break
        else:
            print("This is prime number")
            break


def q14():
    i = 100
    while i < 999:
        order = len(str(i))
        sum = 0

        temp = i
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if i == sum:
            print(i)
        i += 1


def q15():
    number = int(input("Enter few digits: "))

    order = len(str(number))
    sum = 0

    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        print(number, ". This is an ARMSTRONG number")
    else:
        print("This is not an ARMSTRONG number")


def q16():
    number = 200
    while number >= 1:
        temp = number
        reverse = 0

        while (temp > 0):
            remainder = temp % 10
            reverse = (reverse * 10) + remainder

            temp //= 10

        if number == reverse:
            print(number)
        number -= 1


def q17():
    list = []
    number = int(input("Enter a number: "))
    while not number == 0:
        number = int(input("Enter a number: "))

        list.append(number)
        if number == 0:
            print(max(list))

            break


def q18():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    i = 1

    while (num1 >= i <= num2):
        if (num1 % i == 0 and num2 % i == 0):
            val = i
        i += 1

    print("This is the GCD of two numbers: ", val)


def q19():
    num = int(input("Enter number: "))
    i = 2
    while i < num:
        if (num % i) == 0:
            print("This is not a prime number")
            sum = 0
            while num > 0:
                remainder = num % 10
                sum += remainder
                num //= 10
            print("This is the sum-of-digit: ", sum)
            break
        else:
            print("This is prime number")
            i = num
            product = i
            while i >= 2:
                product *= i-1
                i -= 1
            print("The factorial of this prime number is: ", product)
            break


def q20():
    number = int(input("Enter number: "))

    order = len(str(number))
    sum = 0

    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        reversed_number = 0

        while number != 0:
            remainder = number % 10
            reversed_number = reversed_number * 10 + remainder

            number //= 10
        print("This is the reversed number of armstrong number: ", reversed_number)
    else:
        num = number
        reversed_number = 0

        while number > 0:
            remainder = number % 10
            reversed_number = reversed_number * 10 + remainder
            number //= 10

        if reversed_number == num:
            print("This number is a Palindrome as it is not an armstrong number: ", num)


def q21():
    number = int(input("Enter number: "))

    i = number
    facto = i
    while i >= 2:
        facto *= i-1
        i -= 1

    if facto > 500:
        sum = 0
        while facto > 0:
            remainder = facto % 10
            sum += remainder
            facto //= 10
        print(sum)
    else:
        reversed_number = 0

        while facto != 0:
            remainder = facto % 10
            reversed_number = (reversed_number * 10) + remainder

            facto //= 10
        print(reversed_number)
