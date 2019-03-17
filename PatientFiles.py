def anything_else():
    next = input("Would you like to do anything else? Y/N ")
    if next == "Y":
        command = input("What would you like to do? read, change or append? ")
        if command == "read":
            patientID = input("Enter patientID: ")
            with open("PatientChecker/" + patientID + ".txt") as f:
                data = f.read()
                print(data)
            anything_else()
        elif command == "change":
            patientID = input("Enter patientID: ")
            with open("PatientChecker/" + patientID + ".txt", "r") as f:
                lines = f.readlines()
                print(lines)
            with open("PatientChecker/" + patientID + ".txt", "w") as f:
                line = int(input("Which line do you want to edit? "))
                add = input("What would you like to add? (Don't forget to rewrite anything that's already in the line ")
                lines[line] = add + "\n"
                f.write("".join(lines))
            anything_else()
        elif command == "append":
            patientID = input("Enter patientID: ")
            with open("PatientChecker/" + patientID + ".txt", "r") as f:
                lines = f.readlines()
                print(lines)
            with open("PatientChecker/" + patientID + ".txt", "a+") as f:
                add = input("What would you like to add after the last line? ")
                f.write(add + "\n")
            anything_else()
    if next == "N":
        print("Goodbye!")

command = input("What would you like to do? read, change or append? ")
if command == "read":
    patientID = input("Enter patientID: ")
    with open("PatientChecker/" + patientID + ".txt") as f:
        data = f.read()
        print(data)
    anything_else()
elif command == "change":
    patientID = input("Enter patientID: ")
    with open("PatientChecker/" + patientID + ".txt", "r") as f:
        lines = f.readlines()
        print(lines)
    with open("PatientChecker/" + patientID + ".txt", "w") as f:
        line = int(input("Which line do you want to edit? "))
        add = input("What would you like to add? (Don't forget to rewrite anything that's already in the line) ")
        lines[line] = add + "\n"
        f.write("".join(lines))
    anything_else()
elif command == "append":
    patientID = input("Enter patientID: ")
    with open("PatientChecker/" + patientID + ".txt", "r") as f:
        lines = f.readlines()
        print(lines)
    with open("PatientChecker/" + patientID + ".txt", "a+") as f:
        add = input("What would you like to add after the last line? ")
        f.write(add + "\n")
    anything_else()