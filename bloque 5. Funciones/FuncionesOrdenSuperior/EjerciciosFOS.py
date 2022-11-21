import decimal
import string
from functools import reduce
import re
if __name__ == "__main__":
    print("""1. Define una función que devuelva una lista con el doble de todos los elementos de la lista inicial.""")
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    resultado = list(map(lambda x: x * 2, lista))
    print(resultado)

    print("-----------------------------------")
    print("2. Define una función que devuelva que eleve al cuadrado los elementos que sean pares.")
    resultado2 = list(map(lambda x: x ** 2 if x % 2 == 0 else x, lista))
    print(resultado2)

    print("-----------------------------------")
    print("3. Define una función que dada dos listas sume los elementos de la misma posición.")
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista2 = [10, 10, 10, 10, 10, 10, 10, 10, 10]

    resultado3 = list(map(lambda x, y: x + y, lista1, lista2))

    print(resultado3)

    print("-----------------------------------")
    print("""4. Define una funcion que dado una lista de strings devuelva una lista con el numero de ‘a’ que aparece 
    en cada string.""")
    lista3 = ['a', 'sa', 'do']
    resultado4 = sum(map(lambda x: 1 if 'a' in x else 0, lista3))
    print(resultado4)

    print("-----------------------------------")
    print("""5. Define una función que dado una lista sólo devuelva los elementos que son negativos.""")
    lista4 = [1, -2, -3, 4, -5, 6, 7, -8, 9]
    resultado5 = list(filter(lambda x: x < 0, lista4))
    print(resultado5)

    print("-----------------------------------")
    print("""6. Define una función que dado un string devuelva la lista de vocales que aparecen.""")
    lista5 = ['a', 'b', 'e', 'i', 'f', 'ox', 'x']
    resultado6 = list(filter(lambda x: x if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else None, lista5))
    print(resultado6)

    print("-----------------------------------")
    print("""7. Define una función que dado una lista devuelva la multiplicación de todos los elementos.""")
    lista6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    resultado7 = reduce(lambda acumulador, x: x * acumulador, lista6)
    print(resultado7)

    print("-----------------------------------")
    print("8. Dado un string extraer los números que aparecen en el texto y devolver su suma.")
    stringV = 's123asd'
    regex = r'[0-9]'
    numeros = re.findall(regex, stringV)
    newList = list(map(int, numeros))
    print(sum(newList))
