listaElevacion = [4, 2, 0, 3, 2, 5]


def getRain(listE):
    movepeak = 0
    triprain = 0
    maxindex = 0
    for i in range(1, len(listE)):
        if listE[i] > listE[maxindex]:
            maxindex = i
    for i in range(0, len(listE)):
        if movepeak < listE[i]:
            movepeak = listE[i]
        else:
            triprain += movepeak - listE[i]
    movepeak = 0
    for j in range(len(listE) - 1, maxindex, -1):
        if movepeak < listE[j]:
            movepeak = listE[j]
        else:
            triprain += movepeak - listE[j]
    return triprain


if __name__ == '__main__':
    print(getRain(listaElevacion))
