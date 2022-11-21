"""2. Defina una estructura de control que imprima “Todos son igual a 10” si a y b son iguales a 10;
 si no imprima “Sólo a es igual a 10” si a es igual a 10; si no imprima “B es igual a 10” si b es igual a 10;
  si no imprima “Ninguno es igual a 10”."""
a = 100
b = 10

if __name__ == "__main__":
    if a & b == 10:
        print("Todos son igual a 10")
    elif a == 10:
        print("Solo a es igual a 10")
    elif b == 10:
        print("Solo b es igual a 10")
    else:
        print("Ninguno es igual a 10")
