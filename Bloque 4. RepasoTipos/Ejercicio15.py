"""Ejercicio 15
Existiendo dos listas, devolver True si el primer y último elemento de las dos listas son iguales"""
list1 = [1, 2, 3, "Hola"]
list2 = ["1", 2, 3, "adios"]
list3 = ["Quetal", "2", "3", 1]


def findElements(listTocheck1, listTocheck2):
    boolOutput = False
    if listTocheck1[0] == listTocheck2[-1]:
        boolOutput = True
        print(boolOutput)
        return boolOutput
    else:
        boolOutput = False
        print(boolOutput)
        return boolOutput


if __name__ == "__main__":
    findElements(list3, list1)
