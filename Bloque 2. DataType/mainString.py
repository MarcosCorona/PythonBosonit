# string variables
firstVariable = " Master python"

counter = 0
i = 0

output = ""

if __name__ == "__main__":
    print("1. Printing the default variable: ", firstVariable)
    print("--------------------------------------------")

    print("2. Printing the length: ", len(firstVariable))
    print("--------------------------------------------")

    print("3. Printing the first character: ", firstVariable[0])
    print("--------------------------------------------")

    print("4. Printing the penultimate character: ", firstVariable[-1 - 1])
    print("--------------------------------------------")

    print("5. Printing without the first space: ", firstVariable.strip())
    print("--------------------------------------------")

    for i in range(0, len(firstVariable)):
        if i % 2 != 0:
            output = output + firstVariable[i]

    print("6. Printing the odd output: ", output)
    print("--------------------------------------------")

    print("7. Printing lowercase: " + firstVariable.lower())
    print("--------------------------------------------")

    print("8. Separating with blank spaces: ", firstVariable.split())
    print("--------------------------------------------")

    print("9. Replacing python to java: ", firstVariable.replace("python", "JAVA"))
