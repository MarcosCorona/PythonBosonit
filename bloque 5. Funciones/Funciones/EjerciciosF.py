def showAnimal(name, n_legs):
    print(name, n_legs)


def numberOfArgs(*args):
    print(" The number of arguments are: ", len(args))


def calculateArgs(num1, num2):
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)


def calculateMul(param, param1):
    return param * param1


def calculateMod(param, param1):
    return param % param1


def getFuncion(param, param1, param2):
    return param(param1, param2)


def getPersona(name, mail):
    if mail is None:
        print(name, ", Sin determinar.")
    else:
        print(name + ", " + mail)


def numTo0(param):
    amount = param
    while param != 0:
        param -= 1
        amount += param

    print(amount)


if __name__ == "__main__":
    print("""1. Define una función llamada showAnimal que reciba dos argumentos name y n_legs 
    e imprima esta información por pantalla.""")

    showAnimal("perro", 4)

    print("--------------------------------------")
    print("""2. Define una función que puede recibir cualquier número de argumentos e imprima cuántos argumentos ha 
    recibido.""")

    numberOfArgs(1, 2, 4, "hola")

    print("--------------------------------------")
    print("""3. Define una función que recibiendo dos números, devuelva la suma y la resta de ellos en una sola 
    llamada.""")

    calculateArgs(5, 3)

    print("--------------------------------------")
    print("""4. Define una función que recibiendo dos números devuelva la multiplicación.""")
    print("Multiplicacion: ", calculateMul(5, 3))

    print("--------------------------------------")
    print("""5. Define una función que recibiendo dos números devuelva el módulo.""")

    print("Modulo:", calculateMod(8, 3))

    print("--------------------------------------")
    print("""6. Define una función que recibiendo una función del ejercicio 4 o ejercicio 5 y dos valores numéricos 
    devuelva su resultado.""")

    print(getFuncion(calculateMul, 4, 6))

    print("--------------------------------------")
    print("""7. Define una función que reciba el nombre y email de una persona. Si no recibe email, se asignará “Sin 
    determinar”. La función debe imprimir el nombre y email de la persona.""")

    getPersona("Marcos", "marcos@gmail.com")

    print("""8. Define una función que recibiendo un entero positivo, irá sumando este número a su anterior hasta 
    llegar a 0 y devolverá el resultado final.""")

    numTo0(10)
