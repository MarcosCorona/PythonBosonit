"""2. Crear una clase coche que herede de la clase vehículo. Se añaden los atributos numero de puertas y tipo de
gasolina. """
from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, power, consuption, doors, carType):
        self.power = power
        self.consuption = consuption
        self.doors = doors
        self.carType = carType

    def calculateXkm(self):
        print('The consuption per km is: ', self.consuption / 100)

    def __str__(self):
        print("Power:", self.power)
        print("Consuption:", self.consuption)
        print("doors:", self.doors)
        print("Car type:", self.carType)
