"""1. Asigna un valor a la variable i."""

i = 123

if __name__ == "__main__":

    print("""2. Defina una estructura de control que solo imprima i una vez.
     Tienes que usar while sin estados de salida.""")
    while i != i:
        print(i)
    else:
        print(i)

    print("""3. Defina una estructura de control que solo imprima i una vez. 
    Tienes que usar while y estados de salida.""")

    while i == 123:
        print(i)
        i = i+1

    print("""4. Asigna i el valor 0. Crea una estructura de control que vaya incrementando i mientras i sea menor de 10. 
    Comprueba si el valor de i es 6 e imprime “Ejecución terminada” y finaliza el bucle.""")
    i = 0
    while i < 10:
        i += 1
        if i == 6:
            print("Ejecución terminada i:", i)
            i = 10
           
