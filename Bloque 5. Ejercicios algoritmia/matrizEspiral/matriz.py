listM = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def spiralOrder(listMat):
    if not listM:
        return []
    start = 0
    result = []
    row = len(listM)
    column = len(listM[0])
    while row > start * 2 and column > start * 2:
        result += manycolumns(listM, start, row, column)
        start += 1
    return print(result)


def manycolumns(matrix, start, row, column):
    result = []
    endx = row - start - 1
    endy = column - start - 1
    for i in range(start, endy + 1):
        result.append(matrix[start][i])

    if start < endx:
        for i in range(start + 1, endx + 1):
            result.append(matrix[i][endy])
        print('2', result)
    if start < endy and start < endx:
        for i in range(endy - 1, start - 1, -1):
            result.append(matrix[endx][i])
        print('3', result)
    if start < endy and start < endx - 1:
        for i in range(endx - 1, start, -1):
            result.append(matrix[i][start])
        print('4', result)
    return result


if __name__ == "__main__":
    spiralOrder(listM)
