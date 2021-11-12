# Class node implementation
from locale import atoi


class Node:
    def __init__(self, currentnode, g, h, parent):
        self.parent = parent
        self.currentnode = currentnode
        self.g = g
        self.h = h

    def f(self):
        return self.g+self.h


def my_func(initialstate):
    # generating random string with 9 digits to represent all tiles ( 0 for empty tile )
    column = "000111222"
    row = "012012012"
    children = "232343232"
    #  stateHeuristic = calcH(initialState, column, row)
    possiblestates = getChildren(initialstate, column, row, children)
    return possiblestates


def calcH(state, column, row):
    distance = 0
    for index, state in enumerate(state):
        distance += abs(atoi(column[index]) - atoi(column[atoi(state[0])])) + abs(
            atoi(row[index]) - atoi(row[atoi(state[0])]))
        print(distance, state)
    return distance


def getChildren(state, column, row, children):
    children = []
    poszero = getpos(state)
    if column[poszero] == "2":
        tempIndex = poszero - 3
        children.append(swap(state, tempIndex, poszero))
    elif column[poszero] == "0":
        tempIndex = poszero + 3
        children.append(swap(state, tempIndex, poszero))
    else:
        tempIndex = poszero - 3
        children.append(swap(state, tempIndex, poszero))
        tempIndex = poszero + 3
        children.append(swap(state, tempIndex, poszero))

    if row[poszero] == "2":
        tempIndex = poszero - 1
        children.append(swap(state, tempIndex, poszero))
    elif row[poszero] == "0":
        tempIndex = poszero + 1
        children.append(swap(state, tempIndex, poszero))
    else:
        tempIndex = poszero - 1
        children.append(swap(state, tempIndex, poszero))
        tempIndex = poszero + 1
        children.append(swap(state, tempIndex, poszero))
    return children

def swap(string, i, j):
    string = list(string)
    string[i], string[j] = string[j], string[i]
    return ''.join(string)


def getpos(currentstate):
    for i in currentstate:
        if "0" == i:
            return currentstate.index("0")
