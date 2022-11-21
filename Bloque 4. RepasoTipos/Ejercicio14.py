"""Ejercicio 14
Imprime un string con los caracteres de las posiciones en índices pares"""
import string


def pairString(stringVariable) -> string:
    counter = 0
    output = ""
    for i in range(0, len(stringVariable)):
        if i % 2 != 0:
            output = output + stringVariable[i]
            counter += 1
    return print(output)


if __name__ == "__main__":
    pairString(" e s t o   s o n   l a s   p o s i c i o n e s   p a r e s")
