import re

listaToVal = ["(", ")", "{", "}", "[", ")"]


def getValidation(listTV):
    if len(listTV) % 2 != 0:
        return False

    stack = []
    par_dict = {'(': ')', '{': '}', '[': ']'}
    for char in listTV:
        # push opening bracket to stack
        if char in par_dict.keys():
            stack.append(char)
        else:
            # closing bracket without matching opening bracket
            if not stack:
                return False
            # if closing bracket -> pop stack top
            open_brac = stack.pop()
            # not matching bracket -> invalid!
            if char != par_dict[open_brac]:
                return False
    return stack == []


if __name__ == "__main__":
    print(getValidation(listaToVal))
