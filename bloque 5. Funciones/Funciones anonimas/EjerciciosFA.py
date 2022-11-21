if __name__ == "__main__":
    print("""1. Define una función lambda que calcule el cuadrado de un número""")
    square = lambda x: x ** 2
    print(square(2))

    print("------------------------------------------")
    print("""2. Define una función lambda que devuelva True si el cuadrado de un número es mayor que 999 si no 
    devuelve False.""")

    square2 = lambda num: True if num ** 2 > 999 else False
    print(square2(10))

    print("------------------------------------------")
    print("""3. Define una función lambda que reciba dos números y devuelva el resultado de su multiplicación.""")
    multiply = lambda num1, num2: num1 * num2
    print(multiply(2, 3))

    print("------------------------------------------")
    print("""4. Utilizando la función sorted() y lambda ordena una lista de palabras teniendo en cuenta la segunda 
    letra de cada palabra.""")
    wordList = ['pa', 'xc', 'cb']
    wordList.sort(key=lambda x: x[1])
    print(wordList)
