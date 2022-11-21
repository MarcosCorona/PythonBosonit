"""Ejercicio 7
Calcular la suma de los N primeros números pares"""


def calcularSumaPares(n):
    y = 0
    suma = 0
    x = 0
    while y < n:
        if x % 2 == 0 and x != 0:
            suma = suma + x
            y += 1
            x += 1
            print(suma)
        else:
            x += 1


if __name__ == "__main__":
    calcularSumaPares(5)
