import EjercicioClases as ec

if __name__ == "__main__":
    """3. Instancia un objeto con los valores 6 y “Clases y objetos”."""
    v1 = ec.FirstExercise(6, 'patata')

    """4. Añade un método que imprima por pantalla el número."""
    v1.getNumber()

    """5. Crea una clase Circle que dado un radio permita consultar el área, el perímetro y permita modificar el 
    radio. """
    circulo = ec.Circle(2)
    circulo.calcularArea()
    circulo.calcularPerimetro()

    circulo.cambiarRadio(4)
    circulo.calcularArea()
    circulo.calcularPerimetro()

