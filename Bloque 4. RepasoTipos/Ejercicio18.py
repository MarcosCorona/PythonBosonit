"""Ejercicio 18
Calcular el impuesto de cada producto según su precio

De 0 hasta 10.000€ --> 10% impuesto
De 10.001 hasta 24.999€ --> 15% impuesto
A partir de 25.000€ --> 20% impuesto"""


def calculateTaxes(amount):
    totalAmount: 0
    totalTaxes: 0
    if 0 < amount <= 10000:
        taxes = 0.10
        totalTaxes = (amount * taxes)
        totalAmount = totalTaxes + amount
        print("Your taxes:", totalTaxes, "€, your total amount:", totalAmount, "€")
    elif 0 < amount <= 24999:
        taxes = 0.15
        totalTaxes = (amount * taxes)
        totalAmount = totalTaxes + amount
        print("Your taxes:", totalTaxes, "€, your total amount:", totalAmount, "€")
    elif 0 < amount >= 25000:
        taxes = 0.20
        totalTaxes = (amount * taxes)
        totalAmount = totalTaxes + amount
        print("Your taxes:", totalTaxes, "€, your total amount:", totalAmount, "€")
    else:
        print("Your amount is not calculable.")


if __name__ == "__main__":
    calculateTaxes(25000)
