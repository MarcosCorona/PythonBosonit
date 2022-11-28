from Vector import Vector

if __name__ == "__main__":
    vector1 = Vector([45, 65, 23, 4, 34], [6, 32, 8, 82, 77])
    print("---------Min vector---------")
    vector1.minVector()

    print("---------Max vector---------")
    vector1.maxVector()

    print("--------Equal vector----------")
    vector1.eqVector()

    print("---------Coseno---------")
    vector1.cosTwoVectors()

    print("--------Substract----------")
    vector1.substractTwoVectors()

    print("--------Sum----------")
    vector1.sumTwoVectors()

    print("--------Scale----------")
    vector1.scaleProduct()
