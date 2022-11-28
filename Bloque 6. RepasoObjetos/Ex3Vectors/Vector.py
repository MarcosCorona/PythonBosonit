"""Crear mediante la utilización de clases un sistema capaz de lidiar con vectores en 2D, es decir, con el que podamos
 calcular el producto escalar de dos vectores, el coseno del ángulo entre dos vectores y con el que podamos sumar y
 restar vectores (además de compararlos entre sí en términos de módulo). Definir las funciones de producto como métodos
 de un vector al que se le pasa otro vector.

(Se pueden definir las funciones __lt__ y __gt__)."""
import numpy as np
from numpy import dot
from numpy.linalg import norm


class Vector:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def scaleProduct(self):
        print(sum([i * j for (i, j) in zip(self.vector1, self.vector2)]))

    def cosTwoVectors(self, ):
        print(dot(self.vector1, self.vector2) / (norm(self.vector1) * norm(self.vector2)))

    def sumTwoVectors(self):
        print(np.array(self.vector1) + np.array(self.vector2))

    def substractTwoVectors(self):
        print(np.array(self.vector1) - np.array(self.vector2))

    def maxVector(self):
        if self.vector1.__lt__(self.vector2):
            print(self.vector1)
        else:
            print(self.vector2)

    def minVector(self):
        if self.vector1.__gt__(self.vector2):
            print(self.vector1)
        else:
            print(self.vector2)

    def eqVector(self):
        if self.vector1.__eq__(self.vector2):
            print(True)
        else:
            print(False)
