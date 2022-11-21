"""Ejercicio 11
Crear un módulo de validación de nombres de usuario. Las condciones de un nombre de usuario son las siguientes:

Longitud mayor que 6 caracteres.
Longitud menor que 13 caracteres
El nombre de usuario debe ser alfanumérico.
En caso de que el nombre de usuario sea válido se mostrará
por pantalla "Usuario válido". En caso de encontrarnos con algún error."""


def validateUsername(userName):
    if userName.isalnum():
        if 6 < len(userName) < 13:
            print("Username is valid")
        else:
            print("Please check your username")
    else:
        print("userName is not alfanumeric")


if __name__ == "__main__":
    validateUsername('markitos97..')
