list1 = [1, 2, 3, 4, 5]
list2 = ['Hello', 'Word', 'Python']
list3 = ['Operator', 'Membership', 100, 200]
if __name__ == "__main__":
    print("1. Comprueba si 5 está en list1.")
    print("Resultado:", 5 in list1)
    print("-----------------------------------")

    print("2. Comprueba si “Hello” y “Python” están en list2.")
    print("Resultado:", 'Hello' and 'Python' in list2)
    print("-----------------------------------")

    print("3. Comprueba si list2 es igual que list3.")
    print(list2 is list3)
