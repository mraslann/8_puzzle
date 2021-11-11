import Node


def dfs(initialState, goalState):
    stack = set()
    explored = set()
    stack.add(initialState)
    steps = 0
    while stack:
        currentstate = stack.pop()
        explored.add(currentstate)
        steps += 1
        if currentstate == goalState:
            print(currentstate)
            return (currentstate, steps)
        possiblestates = Node.my_func(currentstate)
        for states in possiblestates:
            if (states not in stack) and (states not in explored):
                stack.add(states)
    return "not found", steps
