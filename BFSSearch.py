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


def BFS(current_state, goal_state):
    frontier = set()
    frontier.add(current_state)
    explored = set()
    parent_map = {current_state: 0}
    steps=0
    while frontier:
        state = frontier.pop()
        explored.add(state)
        steps+=1
        if goal_state == state:
            sol=solution(state,parent_map)
            return state,len(sol)
        else:
            neighbours = Node.my_func(state)
            for neighbour in neighbours:
                if (neighbour not in frontier) and (neighbour not in explored):
                    frontier.add(neighbour)
                    parent_map[neighbour] = state
    return "lol"
