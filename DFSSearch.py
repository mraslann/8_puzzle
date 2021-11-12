import Node
#Implementation of DFS search

def dfs(initialState, goalState):
    stack = []
    frontier = set()
    explored = set()
    stack.append(initialState)
    frontier.add(initialState)
    steps = 0
    parent_map = {initialState: 0}
    while stack:
        currentstate = stack.pop()
        explored.add(currentstate)
        steps += 1
        if currentstate == goalState:
            sol = Node.solution(currentstate, parent_map)
            return steps, len(sol), sol
        possiblestates = Node.my_func(currentstate)
        for states in possiblestates:
            if (states not in frontier) and (states not in explored):
                stack.append(states)
                frontier.add(states)
                parent_map[states] = currentstate
