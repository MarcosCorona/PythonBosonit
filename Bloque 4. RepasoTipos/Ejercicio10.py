"""Ejercicio 10
Queremos crear una máquina que de el cambio de lo que han pagado a nuestros clientes.
Supondremos que nuestros depósitos de billetes de cualquier tipo son ilimitados y que el máximo billete es de 50€.
A partir del dinero entregado y el precio de la compra, sacaremos por pantalla el cambio óptimo."""


def getCambio(coste, billete):
    if coste > billete:
        print("Porfavor, dame mi dinero, faltan: ", coste - billete)
    else:
        billete10 = 0
        billete20 = 0
        billete50 = 0

        cambio = 0

        cambioReal = billete - coste

        while cambioReal > cambio:
            if ((cambioReal-cambio) % 50.0) == 0:
                billete50 += 1
                cambio = cambio + 50
            elif ((cambioReal-cambio) % 20) == 0:
                billete20 += 1
                cambio = cambio + 20
            else:
                billete10 += 1
                cambio = cambio + 10

        if billete10 != 0 and billete20 != 0 and billete50 != 0:
            print("Su cambio: ", billete10, "billetes de 10€")
            print("Su cambio: ", billete20, "billetes de 20€")
            print("Su cambio: ", billete50, "billetes de 50€")
        elif billete10 == 0 and billete20 != 0 and billete50 != 0:
            print("Su cambio: ", billete20, "billetes de 20€")
            print("Su cambio: ", billete50, "billetes de 50€")
        elif billete10 == 0 and billete20 == 0 and billete50 != 0:
            print("Su cambio: ", billete50, "billetes de 50€")
        elif billete10 != 0 and billete20 == 0 and billete50 == 0:
            print("Su cambio: ", billete10, "billetes de 10€")
        elif billete10 == 0 and billete20 != 0 and billete50 == 0:
            print("Su cambio: ", billete20, "billetes de 20€")
        elif billete10 != 0 and billete20 == 0 and billete50 != 0:
            print("Su cambio: ", billete10, "billetes de 10€")
            print("Su cambio: ", billete50, "billetes de 50€")
        elif billete10 != 0 and billete20 != 0 and billete50 == 0:
            print("Su cambio: ", billete10, "billetes de 10€")
            print("Su cambio: ", billete20, "billetes de 20€")
        else:
            print("Pago realizado correctamente.")


if __name__ == "__main__":
    getCambio(10.0, 1000)
