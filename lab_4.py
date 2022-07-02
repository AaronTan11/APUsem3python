# This lab questions is about list.

def q1():
    list = []
    i = 1
    while i <= 10:
        prompt = int(input("Enter numbers: "))
        list.append(prompt)
        i += 1

    print(list)
    return


def q2():
    size_of_list = int(input("Enter how many elements of list you want: "))
    count = 1
    list = []
    sum = 0
    while count <= size_of_list:
        questions = int(input("Enter numbers you want to add: "))
        list.append(questions)
        count += 1
    for items in list:
        sum += items
        # print(items)

    print("This is the sum of numbers in the list you entered: ", sum)


def q3():
    number_of_students = int(
        input("Enter the number of students in a class: "))
    list_of_students = []
    count = 1

    while count <= number_of_students:
        student_names = input("Enter student name: ")
        list_of_students.append(student_names)
        count += 1

    print("These are the students: ")
    for student in list_of_students:
        print(student)

    return


def q4():
    number_of_students = int(input("Enter number of students in a class: "))
    list = []
    count = 1
    while count <= number_of_students:
        class_test_marks = int(input("Enter marks of students: "))
        list.append(class_test_marks)
        count += 1

    print(list)
    print("This is the average marks of students class test: ",
          sum(list)/number_of_students)


def q5():
    numberlist = [65, 75, 85, 95, 105]

    prompt = int(input("Enter a number: "))

    for i in numberlist:
        if i == prompt:
            print(prompt, " is in the list of numbers.")
            return
        else:
            print(prompt, " is not in the list of numbers.")
            return

    return


def q6():
    name = input("Enter name of student: ")
    tp_number = input("Enter TP number of student: ")
    subjectmarks = []
    number_of_subjects = int(input("Enter how many subjects there is: "))
    count = 1

    while count <= number_of_subjects:
        marks = int(input("Enter marks of subjects one by one: "))
        subjectmarks.append(marks)
        count += 1
