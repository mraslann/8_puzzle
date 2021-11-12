import Node
#Implementation of BFS search

def BFS(current_state, goal_state):
    queue = []
    frontier = set()
    frontier.add(current_state)
    queue.append(current_state)
    explored = set()
    parent_map = {current_state: 0}
    steps = 0
    while frontier:
        state = queue.pop(0)
        frontier.pop()
        explored.add(state)
        steps += 1
        if goal_state == state:
            sol = Node.solution(state, parent_map)
            return steps, len(sol), sol
        else:
            neighbours = Node.my_func(state)
            for neighbour in neighbours:
                if (neighbour not in frontier) and (neighbour not in explored):
                    frontier.add(neighbour)
                    queue.append(neighbour)
                    parent_map[neighbour] = state
    print("This puzzle has no solution")
    exit(0)
