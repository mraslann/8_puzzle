import time
import heapdict
import cProfile
import pstats


class State:
    def _init_(self, state, cost):
        self.state = state
        self.cost = cost
        self.st = 'u'

    def setSt(self, st):
        self.st = st


def calcF(state, g):
    manhattan_distance = 0
    euclid_distance = 0
    res = [int(x) for x in state]
    for i in res:
        curr_row = res[i] // 3
        curr_column = res[i] % 3
        proj_row = i // 3
        proj_column = i % 3
        x = abs(curr_row - proj_row) + abs(curr_column - proj_column)
        manhattan_distance += x
    return manhattan_distance + g


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
    return currentstate.index("0")


def goalCheck(state):
    if state == "012345678":
        return 1


def solution(state, parent_map):
    sol = []
    cost_to_goal = 0
    while parent_map:
        sol.append(state)
        state, g = parent_map.popitem()
        cost_to_goal += 1
    sol.reverse()
    return sol


def A_star(initialState):
    start_time = time.time()
    currentState = initialState
    g = 0
    expanded = set()
    frontier2 = heapdict.heapdict()
    frontier2[currentState] = calcF(currentState, 0)
    SMap = {currentState: (g, 'f')}
    ParentMap = {}
    while frontier2:
        state, stateCost = frontier2.popitem()
        SMap[state] = 'e'
        expanded.add(state)
        currentState = state
        g = g + 1
        if goalCheck(currentState):
            sol = solution(currentState, ParentMap)
            end_time = time.time()
            runTime = end_time - start_time
            return "Success", len(expanded), len(sol)
        for child in getChildren(currentState, "000111222", "012012012", "232343232"):
            s = SMap.get(child, 'N')
            if child not in SMap:
                ParentMap[child] = (currentState, g)
                frontier2[child] = calcF(child, g)
                SMap[child] = 'f'
            elif s == 'f':
                newChildCost = calcF(child, g)
                Cost = frontier2.get(child)
                if newChildCost < Cost:
                    frontier2._setitem_(child, newChildCost)
                    ParentMap.update((currentState, newChildCost))
    print("Asearch Failed ")
    exit(0)
