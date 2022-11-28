"""Ejercicio 1 Crea una clase vehículo que al instanciarse se le pase la información la potencia y su consumo a los
100 km. Además, crea un método que nos devuelva el consumo por kilómetro """


class Vehicle:
    def __init__(self, power, consuption):
        self.power = power
        self.consuption = consuption

    def calculateXkm(self):
        print('The consuption per km is: ', self.consuption/100)
