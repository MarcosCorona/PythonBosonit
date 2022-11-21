"""Ejercicio 3
Mostrar por pantalla los números del 0 al 10 junto con una anotación que diga si el número es par o impar."""


def esParImpar(x):
    if x % 2 == 0:
        print(x, "es par.")
    else:
        print(x, "es impar.")


if __name__ == "__main__":
    y = 0
    for y in range(11):
        esParImpar(y)
        y += y
