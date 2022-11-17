# List variables
listVariable = [10, 20, 'Hello', 20.5]

text = 20, 40, "bye"
secondList = list(text)
if __name__ == "__main__":
    print("1. Printing default variable: ", listVariable)
    print("--------------------------------------------")

    listVariable.append("World")
    print("2. Adding world at the end of the list: ", listVariable)
    print("--------------------------------------------")

    listVariable.insert(0, "Python")
    print("3. Adding python at the beginning: ", listVariable)
    print("--------------------------------------------")

    print("4. Printing the new list: ", secondList)
    print("--------------------------------------------")

    listVariable.extend(secondList)
    print("5. Joining both lists: ", listVariable)



