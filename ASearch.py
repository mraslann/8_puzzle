import heapdict
import math
import Node

#implemetation of A* search
def calcF(state, g, type):
    #calculating F for A* search where F=G+H
    distance = 0
    res = [int(x) for x in state]
    for i in res:
        curr_row = res[i] // 3
        curr_column = res[i] % 3
        proj_row = i // 3
        proj_column = i % 3
        if type == 'm':
            x = abs(curr_row - proj_row) + abs(curr_column - proj_column)
            distance += x
        elif type == 'e':
            y = math.sqrt(((curr_row - proj_row) ** 2) + (curr_column - proj_column) ** 2)
            distance += y
    return distance + g


def swap(string, i, j):
    string = list(string)
    string[i], string[j] = string[j], string[i]
    return ''.join(string)


def getpos(currentstate):
    return currentstate.index("0")


def goalCheck(state):
    if state == "012345678":
        return 1





def A_star(initialState,type):
    currentState = initialState
    g = 0
    expanded = set()
    frontier2 = heapdict.heapdict()
    frontier2[currentState] = calcF(currentState, 0, type)
    SMap = {currentState: (g, 'f')}
    ParentMap = {currentState:0}
    while frontier2:
        state, stateCost = frontier2.popitem()
        SMap[state] = 'e'
        expanded.add(state)
        currentState = state
        g = g + 1
        if goalCheck(currentState):
            sol = Node.solution(currentState, ParentMap)
            return len(expanded), len(sol), sol
        for child in Node.getChildren(currentState, "000111222", "012012012", "232343232"):
            s = SMap.get(child, 'N')
            if child not in SMap:
                ParentMap[child] = (currentState)
                frontier2[child] = calcF(child, g,type)
                SMap[child] = 'f'
            elif s == 'f':
                newChildCost = calcF(child, g,type)
                Cost = frontier2.get(child)
                if newChildCost < Cost:
                    frontier2._setitem_(child, newChildCost)
                    ParentMap.update((currentState, newChildCost))
