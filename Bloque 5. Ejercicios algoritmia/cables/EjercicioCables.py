input1 = "HM"

input2 = "HH"

input3 = "MM"


def testCables(c1, c2, c3):
    if c1[0] != c2[-1] and c1[-1] != c2[0] \
            or c2[0] != c1[0] and c2[-1] != c1[0] \
            and c1[0] != c3[-1] and c1[-1] != c3[0] \
            or c3[0] != c1[0] and c3[-1] != c1[0] \
            and c2[0] != c3[-1] and c2[-1] != c3[0] \
            or c3[0] != c2[-1] and c3[-1] != c2[0]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(testCables(input1, input2, input3))
