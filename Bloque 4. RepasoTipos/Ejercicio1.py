# Ejercicios repaso tipos y operadores
# if_exercises
# Calcular el área y el volumen de un cilindro de 2 m de radio y 3 m de altura. Se puede utilizar π
# como una variable más escribiendo math.pi.
import math


def calculateArea(radiusToC, heightToC):
    result = 2 * math.pi * radiusToC * (heightToC + radiusToC)
    print("The area of the cylinder is:", result.__round__(2))


def calculateVol(radiusToC, heightToC):
    volume = (math.pi * (radiusToC ** 2)) * heightToC
    print("The volume of the cylinder is: ", volume.__round__(2))


if __name__ == "__main__":
    radius = 2
    height = 3
    calculateArea(radius, height)

    calculateVol(radius, height)
