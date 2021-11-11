import Node


def dfs(initialState, goalState):
        stack = []
        popped = []
        explored = set()
        stack.append(initialState)
        steps = 0
        while stack:
                currentstate = stack.pop()
                # print("popped", currentstate)
                explored.add(currentstate)
                # print("stack is", stack)
                # print("explored is ", explored)
                # print("")
                steps += 1
                if currentstate == goalState:
                        print(currentstate)
                        return ("found", steps)
                # Node.Node(currentstate, 0, 0, None)
                possiblestates = Node.my_func(currentstate)
                for states in possiblestates:
                        if (states not in stack) and (states not in explored):
                                stack.append(states)
        return "not found", steps
