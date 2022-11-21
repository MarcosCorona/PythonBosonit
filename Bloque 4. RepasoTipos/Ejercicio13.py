"""Ejercicio 13
Crear un módulo de validación de DNI con expresiones regulares (regex). Las condiciones del DNI deben de ser las siguientes:

El DNI debe de contener exactamente 9 caracteres. Los 8 primeros caracteres del DNI deben de ser números. El caracter
final del DNI debe de ser una letra. Si el DNI es válido, se mostrará un mensaje por pantalla "DNI Válido". De lo
contrario se mostrará un mensaje de error. """
import re

REGEXP = "[0-9]{8}[A-Z]"
digit_control = "TRWAGMYFPDXBNJZSQVHLCKE"


def validateDni(dni):
    if re.match(REGEXP, dni) is not None and dni[8] == digit_control[int(dni[0:8]) % 23]:
        print("Dni valid.")
    else:
        print("Dni is invalid")


if __name__ == "__main__":
    validateDni("50561829D")
