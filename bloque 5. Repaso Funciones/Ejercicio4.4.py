"""Ejercicio 4.4
Dada una lista con listas anidadas en su interior, devolver una lista que no esté anidada."""

lista = [1, 43, [1, 7, 6, ['uno', 'dos'], 'Madrid'], 'Tortuga']


def listasNoAnidadas(oldList):
    letsee = list(map(lambda x: x if type(x) is not list else None, oldList))
    return letsee


if __name__ == "__main__":
    print(listasNoAnidadas(lista))
