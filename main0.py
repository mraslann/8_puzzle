import DFSSearch
import time
import random
import BFSSearch
import ASearch

#generation of random initial states
goalState = "012345678"
initialstate = ''.join(random.sample("120345678", 9))
print("Initial state is ", initialstate)

#using bfs to search
starttime = time.time()
steps, soldepth, path = BFSSearch.BFS(initialstate, goalState)
endtime = time.time()
print("BFS:\nRunning time: " + str("{:.2f}".format(endtime-starttime)) + " seconds \nNodes expanded: "
      + str(steps) + " nodes \nMaximum depth: ", soldepth, "\nCost: ", soldepth, "\nPath to goal: ", path)

#using dfs to search
starttime = time.time()
steps, soldepth, path = DFSSearch.dfs(initialstate, goalState)
endtime = time.time()
print("DFS:\nRunning time: " + str("{:.2f}".format(endtime-starttime)) + " seconds \nNodes expanded: "
      + str(steps) + " nodes \nMaximum depth: ", soldepth, "\nCost: ", soldepth, "\nPath to goal: ", path)

#using A* (manhattan heuristic) to search
starttime = time.time()
steps1, soldepth1, sol1 = ASearch.A_star(initialstate, 'm')
endtime = time.time()
print("A* Manhattan:\nRunning time: " + str("{:.2f}".format(endtime-starttime)) + " seconds \nNodes expanded: "
      + str(steps1) + " nodes \nMaximum depth: ", soldepth1, "\nCost: ", soldepth1, "\nPath to goal: ", sol1)

#using A* (euclidian heuristic) to search
starttime = time.time()
steps2, soldepth2, sol2 = ASearch.A_star(initialstate, 'e')
endtime = time.time()
runningtime = endtime - starttime
print("A* Euclidian:\nRunning time: " + str("{:.2f}".format(endtime-starttime)) + " seconds \nNodes expanded: "
      + str(steps2) + " nodes \nMaximum depth: ", soldepth2, "\nCost: ", soldepth2, "\nPath to goal: ", sol2)
