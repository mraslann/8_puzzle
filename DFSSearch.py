import Node


def solution(state, parent_map):
    sol = []
    cost_to_goal = 0
    while parent_map[state]:
        sol.append(state)
        state = parent_map[state]
        cost_to_goal += 1
    sol.reverse()
    sol.append(cost_to_goal)
    return sol


def dfs(initialState, goalState):
    stack = set()
    explored = set()
    stack.add(initialState)
    parent_map = {initialState: 0}
    steps = 0
    while stack:
        currentstate = stack.pop()
        explored.add(currentstate)
        steps += 1
        if currentstate == goalState:
            sol=solution(currentstate, parent_map)
            return currentstate, len(sol) - 1
        possiblestates = Node.my_func(currentstate)
        for states in possiblestates:
            if (states not in stack) and (states not in explored):
                stack.add(states)
                parent_map[states] = currentstate
    return "not found", steps
