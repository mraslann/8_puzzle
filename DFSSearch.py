import Node


def solution(state, parent_map):
    sol = []
    cost_to_goal = 0
    while parent_map[state]:
        sol.append(state)
        state = parent_map[state]
        cost_to_goal += 1
    sol.reverse()
    return sol


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
            sol = solution(currentstate, parent_map)
            print("final state (goal state) is ", currentstate)
            return "Success", steps, len(sol), sol
        possiblestates = Node.my_func(currentstate)
        for states in possiblestates:
            if (states not in frontier) and (states not in explored):
                stack.append(states)
                frontier.add(states)
                parent_map[states] = currentstate
    return "Failed", steps, 0, 0

