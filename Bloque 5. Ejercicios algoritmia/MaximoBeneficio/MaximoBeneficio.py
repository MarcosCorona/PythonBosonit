listaPrecios = [7, 1, 5, 3, 6, 4]


def getBeneficio(listaP):
    beneficio = 0
    acBen = 0
    precioMaxBen = 0
    counter = 0
    for p in listaP:
        if counter == 0:
            pass
        elif p - listaP[counter - 1] > 0:
            acBen = p - listaP[counter - 1]
            if acBen >= beneficio:
                beneficio = acBen
                precioMaxBen = p
        else:
            acBen = 0
        counter += 1
    return f"El máximo beneficio es de: {beneficio} € con el valor de: {precioMaxBen} €"


if __name__ == "__main__":
    print(getBeneficio(listaPrecios))
