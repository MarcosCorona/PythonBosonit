"""1. Define una clase vacía llamada FirstExercise."""
import math


class FirstExercise:
    """Modifica la clase anterior. La clase debe recibir obligatoriamente las variables number y chapter."""

    def __init__(self, number, character):
        self.number = number
        self.character = character

    def getNumber(self):
        print(self.number)


"""5. Crea una clase Circle que dado un radio permita consultar el área, el perímetro y permita modificar el radio."""


class Circle:

    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        area = 2 * math.pi * self.radio
        print('Area:', area)

    def calcularPerimetro(self):
        perimetro = math.pi * (self.radio ** 2)
        print('Perimetro:', perimetro)

    def cambiarRadio(self, newRadio):
        self.radio = newRadio
        print('Nuevo radio:', self.radio)
