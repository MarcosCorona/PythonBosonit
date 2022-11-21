"""Ejercicio 16
Dado una lista devolver otra lista con los elementos que son divisibles entre 5"""

inputList = [66, 5, 2, 15, 200]
outputList = []


def getDivisorOf5(checkingList):
    for element in checkingList:
        if element % 5 == 0:
            outputList.append(element)
        else:
            pass
    print(outputList)


if __name__ == "__main__":
    getDivisorOf5(inputList)
    x = 2

