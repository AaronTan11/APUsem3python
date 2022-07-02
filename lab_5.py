x = 0
y = 0
num1 = x
num2 = y


def addition():
    print(num1 + num2)


def subtraction():
    print(num1 - num2)


def division():
    print(num1 / num2)


def multiplication():
    print(num1 * num2)


# Write a Python code to accept 2 values from user and display addition of those values by using function.


def q1():
    global num1, num2
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    addition()


# Write a Python code to do all Arithmetic operations by using function.


def q2():
    global num1, num2
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    get_oper = input(
        "Choose one Arithmetic Operation: \n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\nSelect your option: ")

    operation = {
        '1': addition,
        '2': subtraction,
        '3': division,
        '4': multiplication
    }
    operation.get(get_oper)()


def q3():
    numberlist = [65, 75, 85, 95, 105]

    def check_number():
        prompt = int(input("Enter a number: "))

        for i in numberlist:
            if i == prompt:
                print(prompt, " is in the list of numbers.")
                return
            else:
                print(prompt, " is not in the list of numbers.")
                return

        return
    check_number()
