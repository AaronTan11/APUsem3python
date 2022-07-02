print('--------------------------')
print('Welcome To Lab 1 @python--')
print('--------------------------')


def first_question():
    print("Hello")


def second_question():
    x = 5
    print(x)


def third_question():
    x = input("Enter number: ")
    print(x)


def fourth_question():
    x, y = int(input("Enter a number: ")), int(input("Enter another number: "))
    print(x + y)


def sixth_question():
    x, y = int(input("Enter a number: ")), int(input("Enter another number: "))
    z = x
    x, y = y, z

    print(x, y)


def fifth_question():
    x, y = int(input("Enter a number: ")), int(input("Enter another number: "))

    chooseOperation = input(
        "Choose an operation(add,subtract,multiply,divide, modulo): ")
    if chooseOperation == "add":
        results = x + y
    elif chooseOperation == "subtract":
        results = x - y
    elif chooseOperation == "multiply":
        results = x * y
    elif chooseOperation == "divide":
        results = x / y
    elif chooseOperation == "modulo":
        results = x % y

    print(f"{results:.2f}")


def eight_question():
    eng, bm, math, phy, chem = [int(x) for x in input(
        'Enter your mark for ENG, BM, MATH, PHY, CHEM accordingly: ').split()]
    total_marks = int(eng + bm + math + phy + chem)
    average_percentage = total_marks / 5
    print(
        f"Total Mark: {total_marks:.2f}%\nAverage Mark: {average_percentage:.2f}%")


def seventh_question():
    radius, unit = int(input("Enter radius: ")), input("Enter your Unit: ")
    aoc = 3.14 * (radius * radius)
    coc = 2 * 3.14 * radius
    print(
        f"Area of Circle: {aoc:.2f} {unit}\nCircumference of Circle: {coc:.2f} {unit}")


def ninth_question():
    basic = int(input("Enter your Basic salary: "))
    grade_pay, DA, TA, HRA = (basic * 2), (0.7 * basic), (200), (0.2 * basic)
    total_salary = grade_pay + DA + TA + HRA
    print(f"RM {total_salary:.2f}")


def test():
    x, y = int(input("Enter x number: ")), int(input("Enter y number: "))
    choice = input("Choose add or subtract: ")

    def add():
        print(x+y)

    def subtract():
        print(x - y)

    def notAfunc():
        print("idk what this")

    operations_select = {
        "add": add,
        "subtract": subtract
    }.get(choice, notAfunc)()
