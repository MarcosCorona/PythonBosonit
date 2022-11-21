"""3. Defina una estructura de control que imprima “A y B son impares” si tanto a como b son impares;
si no imprima “A y B no son impares”."""
a = 101
b = 1001

if __name__ == "__main__":
    if a % 2 == 0 and b % 2 == 0:
        print("Tanto a como b son pares")
    else:
        print("Tanto a como b son impares")
