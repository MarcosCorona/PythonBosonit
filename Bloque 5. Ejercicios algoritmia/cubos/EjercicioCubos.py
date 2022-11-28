cubo1 = input("Cantidad cubo 1:")
cubo2 = input("Cantidad cubo 2:")
cubo3 = input("Cantidad cubo 3:")


def calcularLlenado(c1, c2, c3):
    calculo = 0
    if c1 > c2 and c1 > c3:
        calculo = (c1 - c2) + (c1 - c3)
    elif c2 > c1 and c2 > c3:
        calculo = (c2 - c1) + (c2 - c3)
    elif c3 > c2 and c3 > c1:
        calculo = (c3 - c2) + (c3 - c1)

    return calculo


if __name__ == "__main__":
    print(calcularLlenado(int(cubo1), int(cubo2), int(cubo3)))
