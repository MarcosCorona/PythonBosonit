# set variables

firstVariable = {"coche", "motocicleta", "bicicleta"}

secondVariable = set(("avión", "coche", "tractor"))

if __name__ == "__main__":
    print("1. Print default variable: ", firstVariable)
    print("--------------------------------------------")

    firstVariable.add("avión")
    print("2. Print variable with an add: ", firstVariable)
    print("--------------------------------------------")

    firstVariable.remove("coche")
    print("3. Print variable with delete: ", firstVariable)
    print("--------------------------------------------")

    print("4. Printing second variable with set: ", secondVariable)
    print("--------------------------------------------")

    thirdVariable = firstVariable.difference(firstVariable.difference(secondVariable))
    print("5. Printing the third variable: ", thirdVariable)
    print("--------------------------------------------")

    print("6. joining 2 variables: ", firstVariable.union(secondVariable))
