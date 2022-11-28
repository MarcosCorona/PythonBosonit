"""Ejercicio 1 Define una función que devuelva las palabras de entre 3 y 5 letras que no tienen la letra o. Úsala con
la variable texto. """
import re

texto = "En un lugar, de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de " \
        "los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. "


def getWords(text):
    regex = re.split(" ", text)
    newList = []
    wordsList = list(map(lambda x: newList.append(x) if 3 <= len(x) <= 5 and 'o' not in x else None, regex))
    return newList


if __name__ == "__main__":
    print(getWords(texto))
