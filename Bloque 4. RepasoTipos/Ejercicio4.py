"""Ejercicio 4
Mostrar por pantalla las tablas de multiplicar del 7, el 8 y el 9. El formato debe ser "7x1 = 7"""


def tablaDeX(x):
    y = 0
    for y in range(11):
        print(x, "x", y, "=", x * y)


if __name__ == "__main__":
    tablaDeX(7)
    print("-------------")
    tablaDeX(8)
    print("-------------")
    tablaDeX(9)
