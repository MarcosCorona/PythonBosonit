"""Ejercicio 12
Crear un módulo de validación de contraseñas. La contraseña debe cumplir los siguientes requisitos:

La contraseña debe tener un mínimo de 8 caracteres. La contraseña debe contener mayúsculas, minúsculas, números y al
menos un caracter no alfanumérico. La contraseña no debe tener espacios en blanco. Si la contraseña es válida se
mostrará un mensaje por pantalla y en caso de no serlo se mostrarán los requisitos incumplidos. """
import re


def passwordValidate(password):
    if len(password) < 8:
        print("Password must have <8 digits")
    elif not any(char.isdigit() for char in password):
        print("Password should have at least 1 number.")
    elif not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
    elif not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
    elif re.search("[$@#.-]", password) is None:
        print('Password should have at least one of the symbols $@#')
    elif any(char.isspace() for char in password):
        print('Password should not have spaces.')
    else:
        print("Password saved.")


if __name__ == "__main__":
    passwordValidate("PassWord $2")
