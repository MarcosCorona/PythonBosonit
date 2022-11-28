"""1. Cree una clase Vehicle que reciba el nombre, velocidad máxima y el kilometraje."""


class Vehicle:
    owner = 'Bosonit'

    def __init__(self, name, maxSpeed, km):
        self.name = name
        self.maxSpeed = maxSpeed
        self.km = km

    def getCapacity(self, capacity):
        print(f"Capacity of {self.name} is {capacity}")

    def __str__(self):
        print("Name:", self.name)
        print("Max Speed:", self.maxSpeed)
        print("KM:", self.km)
        print("Owner:", self.owner)
