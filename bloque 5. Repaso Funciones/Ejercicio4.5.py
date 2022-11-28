"""Ejercicio 4.5 Implementar una función que lleve a cabo el cifrado César de una frase. El cifrado se lleva a cabo
de la siguiente manera:

Para cada letra de la palabra (sin distinguir mayúsculas y minúsculas) obtenemos su orden dentro del alfabeto.
A ese valor le sumaremos el valor de la clave dada por el usuario.
Sustituiremos la letra original por la que esté en esta nueva posición calculada dentro de nuestro alfabeto."""

texto = input("tu texto:  ")


def codificar(mensaje, rotaciones):
    # Nota: también se puede importar a string y usar ascii_letters y ascii_uppercase
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        # Rotamos la letra
        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        codificado += alfabeto_a_usar[posicion]
    return print(codificado)


if __name__ == "__main__":
    codificar(texto, 2)
