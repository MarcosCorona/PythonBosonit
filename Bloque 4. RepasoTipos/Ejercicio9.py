"""Ejercicio 9
Dado un número entero  𝑛 , comprobar si el número es primo."""


def esPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True


if __name__ == "__main__":
    esPrimo(8)
