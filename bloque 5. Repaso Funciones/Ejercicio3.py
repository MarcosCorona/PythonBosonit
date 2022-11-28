"""Ejercicio 3 La serie de Fibonacci es una conocida serie en la que cada elemento se calcula como la suma de los dos
anteriores, empezando por 1 1, es decir: """


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


if __name__ == "__main__":
    m = int(input("Ingresa límite moxios de la sucesión: "))
    fib(m)
