"""Ejercicio 8
Calcular el máximo, el mínimo y la media de una lista de enteros."""
from statistics import mean


def addNumList(x):
    numList = []
    for y in range(x):
        numList.append(y)
        y += 1
    print("Average:", mean(numList))
    print("Minimus:", min(numList))
    print("Maximus:", max(numList))


if __name__ == "__main__":
    addNumList(101)
