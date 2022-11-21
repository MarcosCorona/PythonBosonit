import math

"""Ejercicio 17
Devolver True si el número recibido es un palíndromo"""


def testPalindromo(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(testPalindromo(96969692))
