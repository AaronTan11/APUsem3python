print('--------------------------')
print('Welcome To Lab 2 @python--')
print('--------------------------')


def Question1():
    number = int(input("ENter A nUmber: "))
    results = number % 2

    if results == 0:
        print("THIS IS AN EVEN NUMBERRR!!!")
    else:
        print("THIS IS AN ODDD NUMBERRR!!!")


def Question2():
    year = int(input("Enter a year: "))
    results = year % 4

    if results == 0:
        print("THIS IS A LEAP YEAR!!!")
    else:
        print("THIS IS NOT A LEAP YEAR!!!")


def Question3():
    x, y = int(input("ENter a number:")), int(input("Enter another number: "))

    if x > y:
        print(f"The largest number is: {x}")
    else:
        print(f"The largest number is: {y}")


def Question4():
    x, y, z = int(input("ENter a number:")), int(
        input("Enter another number: ")), int(input("Enter ANOTHER ONEE: "))

    if x > y > z:
        print(f"The largest number is: {x}")
    elif y > x > z:
        print(f"The largest number is: {y}")
    else:
        print(f"The Largest Number is: {z}")


def Question5():
    number = int(input("Enter a number from Positive to Negative: "))

    if number > 0:
        print("This is a Positive number!!")
    elif number < 0:
        print("This is a NEGATIVE number!!")
    else:
        print("This is just an egg '0'")


def Question6():
    studentName = input("Enter Your Name: ")
    tpNumber = input("Enter Your TP Number: ")
    python = float(input("Enter your Python marks: "))
    eim = float(input("Enter your EIM marks: "))
    dsa = float(input("Enter your DSA marks: "))
    csa = float(input("Enter your CSA marks: "))
    os = float(input("Enter your OS marks: "))
    total = python + eim + csa + os + dsa
    percentage = total / 5

    if 80 <= total <= 100:
        print("Grade: A+")
    elif 75 <= total <= 79:
        print("Grade: A")
    elif 70 >= total <= 74:
        print("Grade: B+")
    elif 65 >= total <= 69:
        print("Grade: B")
    elif 60 >= total <= 64:
        print("Grade: C+")
    elif 55 >= total <= 59:
        print("Grade: C")
    elif 50 >= total <= 54:
        print("Grade: C-")
    elif total < 50:
        print("Grade: D")
    print(f"Student Name: {studentName}")
    print(f"Total Marks: {total:.2f}%\nAverage Marks: {percentage:.2f}%")
    print(f"TP Number: {tpNumber}")


def Question7():
    name = input("Enter your Name: ")
    purchaseAmount = float(input("Enter purchase amount: RM "))
    taxCode = int(input("Enter your Tax Code(0,1,2,3): "))

    if taxCode == 1:
        salesTax = 0.03 * purchaseAmount

    elif taxCode == 2:
        salesTax = 0.05 * purchaseAmount

    elif taxCode == 3:
        salesTax = 0.07 * purchaseAmount

    elif taxCode == 0:
        salesTax = 0 * purchaseAmount
    totalAmountDue = salesTax + purchaseAmount
    print(f"Name: {name}")
    print(f"Purchase Amount: RM {purchaseAmount:.2f}")
    print(f"Sales Tax: {salesTax:.2f}")
    print(f"Total Amount: RM {totalAmountDue:.2f}")


def Question8():
    temp = float(input("Enter your Temperature: "))

    if temp > 38 or temp < 36:
        print("You Are SIck!!! GO to SunMED NOWW!!")


def Question9():
    name = input("Enter your NAMEE: ")
    purchaseAmount = float(input("ENter Purchase Amount: "))

    if purchaseAmount > 300:
        totalBill = purchaseAmount - 0.1 * purchaseAmount
    elif purchaseAmount <= 300 or purchaseAmount >= 201:
        totalBill = purchaseAmount - 0.4 * purchaseAmount
    elif purchaseAmount <= 200 or purchaseAmount >= 101:
        totalBill = purchaseAmount - 0.3 * purchaseAmount
    elif purchaseAmount >= 0 or purchaseAmount <= 100:
        totalBill = purchaseAmount - 0.2 * purchaseAmount

    print(f"Name: {name}")
    print(f"Purchase Amount: {purchaseAmount}")
    print(f"Total Bill: RM {totalBill:.2f}")
