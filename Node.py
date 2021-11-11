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

# def converttostring(current):
#     # initialize an empty string
#     str = ""
#     # traverse in the string
#     for i in current:
#         str += i
#
#         # return string
#     return str
#
#
# # function to get the posistion of an element in the state
# def getpos(currentstate):
#     for i in currentstate:
#         if i == "0":
#             return currentstate.index(i)
#
#
# def generatepossiblestates(currentstate):
#     possiblestates = []
#     position = getpos(currentstate)
#
#     if position == 4:
#         j = 1
#         for i in range(0, 4):
#             current = list(currentstate)
#             current[j], current[4] = current[4], current[j]
#             current = converttostring(current)
#             possiblestates.append(current)
#             j = j + 2
#
#     else:
#         if position == 0:
#             j = 1
#             for i in range(0, 2):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 j = j + 2
#
#         if position == 1:
#             j = 0
#             for i in range(0, 3):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 j = j + 2
#
#         if position == 2:
#             j = 1
#             for i in range(0, 2):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 j = j + 4
#
#         if position == 3:
#             j = 0
#             for i in range(0, 3):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 if j == 0:
#                     j = 4
#                 else:
#                     j = j+2
#
#         if position == 5:
#             j = 2
#             for i in range(0, 3):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 if j == 4:
#                     j = j + 4
#                 else:
#                     j = j + 2
#
#         if position == 6:
#             j = 3
#             for i in range(0, 2):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 j = j + 4
#
#         if position == 7:
#             j = 4
#             for i in range(0, 3):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 j = j + 2
#
#         if position == 8:
#             j = 5
#             for i in range(0, 2):
#                 current = list(currentstate)
#                 current[j], current[position] = current[position], current[j]
#                 current = converttostring(current)
#                 possiblestates.append(current)
#                 j = j + 2
#     return possiblestates


def my_func(initialstate):
    # generating random string with 9 digits to represent all tiles ( 0 for empty tile )
    goal = "012345678"
    column = "000111222"
    row = "012012012"
    children = "232343232"
    #  stateHeuristic = calcH(initialState, column, row)
    possiblestates = getChildren(initialstate, column, row, children)
    return possiblestates


def calcH(state, column, row):  #O(n)
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
        Ctemppos = atoi(column[poszero]) - 1
        tempIndex = poszero - 3
        children.append(swap(state, tempIndex, poszero))
    elif column[poszero] == "0":
        Ctemppos = atoi(column[poszero]) + 1
        tempIndex = poszero + 3
        children.append(swap(state, tempIndex, poszero))
    else:
        Ctemppos = atoi(column[poszero]) - 1
        tempIndex = poszero - 3
        children.append(swap(state, tempIndex, poszero))
        Ctemppos = atoi(column[poszero]) + 1
        tempIndex = poszero + 3
        children.append(swap(state, tempIndex, poszero))

    if row[poszero] == "2":
        Rtemppos = atoi(row[poszero]) - 1
        tempIndex = poszero - 1
        children.append(swap(state, tempIndex, poszero))
    elif row[poszero] == "0":
        Rtemppos = atoi(row[poszero]) + 1
        tempIndex = poszero + 1
        children.append(swap(state, tempIndex, poszero))
    else:
        Rtemppos = atoi(row[poszero]) - 1
        tempIndex = poszero - 1
        children.append(swap(state, tempIndex, poszero))
        Rtemppos = atoi(row[poszero]) + 1
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
            return currentstate.index(i)
