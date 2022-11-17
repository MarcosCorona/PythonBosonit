# dictionary variables
firstDict = dict(coche=10), dict(motocicleta=20), dict(camion=30)

secondDict = {
    "coche": 10,
    "motocicleta": 20,
    "camión": 30
}

vehicles = ["coche", "motocicleta", "camion"]
units = [10, 20, 30]
thirdDict = dict(zip(vehicles, units))
if __name__ == "__main__":
    print("1. Printing first dictionary: ", firstDict)
    print("--------------------------------------------")

    print("2. Printing second dictionary: ", secondDict)
    print("--------------------------------------------")

    print("3. Printing third dictionary: ", thirdDict)
    print("--------------------------------------------")

    print("4. Showing the third dictionary values: ", thirdDict.values())
    print("--------------------------------------------")

    print("5. Showing the third dictionary keys: ", thirdDict.keys())
    print("--------------------------------------------")

    print("6. Showing the car value: ", thirdDict.get("coche"))
    print("--------------------------------------------")
    thirdDict["avion"] = 100
    print("7/8. Adding a value to the dictionary: ", thirdDict)


