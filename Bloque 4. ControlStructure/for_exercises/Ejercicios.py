from operator import index

a = ['Hello', 'World.']
b = ['Python', 3.9]
c = "HelloWordPython"
v1 = ''
v2 = ''
if __name__ == "__main__":

    print("1. Recorre todos los caracteres de c e imprimelos por pantalla.")

    for x in c:
        print(x)
    print("----------------------------------------------------------")
    print("2. Muestra todos los valores de a.")

    for x in a:
        print(x)
    print("----------------------------------------------------------")
    print("""3. Muestra cada valor de a y b mostrando cada elemento de a con el de la misma posición de b 
    sin utilizar los índices de posición.""")

    for x, y in zip(a, b):  # obtenemos los valores en cada iteración
        print(x, y)

    print("----------------------------------------------------------")
    print("""4. Muestra en cada iteración el valor y su índice para los elementos de b.""")
    for x in b:
        print(x, b.index(x))
