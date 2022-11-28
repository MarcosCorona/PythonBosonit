"""Ejercicio 4.6
Calcular la desviación estándar de una lista que será nuestra población. La desviación estandar (
σ
) se puede calcular mediante la expresión
 es la media de la población. Hacerlo utilizando map y reduce."""
import math
from functools import reduce

list = [12, 24, 36, 48, 60]


def calcularDesviacion(poblacion):
    mean2 = sum(map(lambda x: x / len(poblacion), poblacion))
    mean3 = sum(map(lambda x: (x - mean2) ** 2 / len(poblacion), poblacion))
    #mean4 = reduce(lambda acumulado, x: acumulado + x + (x - mean2) ** 2 / len(poblacion), poblacion)

    desviacion = math.sqrt(mean3)

    return print(desviacion)


if __name__ == "__main__":
    calcularDesviacion(list)
