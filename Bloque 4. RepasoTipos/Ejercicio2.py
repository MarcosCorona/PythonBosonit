"""Ejercicio 2
Resolver la ecuación

7x^2+21x−28=0
y mostrar por pantalla el resultado."""
from math import sqrt

a = 7
b = 21
c = -28

if __name__ == "__main__":
    x1 = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)

    print("Resultado 1:", x1)
    print("Resultado 2:", x2)
