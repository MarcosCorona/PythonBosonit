"""Ejercicio 2
Crea una función que devuelva el porcentaje de elementos únicos de una lista."""
import re

lista = [1, 2, 4, 5, 1, 1, 'Hola', 'pato', 'Hola', 'Logroño']


def obtainUnicNumbers(oldList):
    unicos = []
    regex = "[0-9]"
    numeros = re.findall(regex, str(oldList))
    for numero in numeros:
        if numero not in unicos:
            unicos.append(numero)
    return unicos


if __name__ == "__main__":
    print(obtainUnicNumbers(lista))
