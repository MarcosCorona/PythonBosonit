import Vehicle

"2. Cree una clase Bus que herede todos los métodos y variables de Vehicle."


class Bus(Vehicle):
    def __init__(self, name, maxSpeed, km):
        self.name = name
        self.maxSpeed = maxSpeed
        self.km = km

    def getCapacity(self, capacity):
        capacity = 50
        print(f"Capacity of {self.name} is {capacity}")
