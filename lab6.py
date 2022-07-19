def q1():
    db = open("flightdb.txt", "w")
    masterList = []

    for i in range(1, 6):
        flightList = []

        name = input("Enter name: ")
        departure = input("Enter depart country and destination: ")

        flightList.append(name)
        flightList.append(departure)

        for x in flightList:
            db.write(x)
            db.write(", ")
        db.write("\n")


q1()
