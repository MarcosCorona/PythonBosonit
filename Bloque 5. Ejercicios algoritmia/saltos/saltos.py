jumpList = [2, 3, 1, 1, 4]


def canJump(jumpL):
    len_nums = len(jumpL)
    maxJumps = 0
    for i, num in enumerate(jumpL):
        if i == 0:
            maxJumps = i + num
        elif maxJumps >= i:
            maxJumps = (max(i + num, maxJumps))
        else:
            return False
        if maxJumps >= len_nums - 1:
            return True
        print(maxJumps)


if __name__ == "__main__":
    canJump(jumpList)
