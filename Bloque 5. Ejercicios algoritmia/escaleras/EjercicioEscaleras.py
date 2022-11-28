de1 = 1
de2 = 2

numEscaleras = 4

formas = [1, 2]


def calcularPosibilidades(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in X:
        return 1 + sum(calcularPosibilidades(n - x, X) for x in X if x < n)
    else:
        return sum(calcularPosibilidades(n - x, X) for x in X if x < n)


if __name__ == "__main__":
    print(calcularPosibilidades(numEscaleras, formas))
