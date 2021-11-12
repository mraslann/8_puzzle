import DFSSearch
import time
import random
import BFSSearch
import ASearch


goalState = "012345678"
initialstate = ''.join(random.sample("012345678", 9))
print("initialstate is ", initialstate)

starttime = time.time()
bfs, steps, soldepth, path = BFSSearch.BFS(initialstate, goalState)
endtime = time.time()
print("(bfs)" + bfs + " in time " + str("{:.2f}".format((endtime-starttime))) + " seconds and in "
      + str(steps) + " nodes expanded and depth ", soldepth, "and path to goal", path)

starttime = time.time()
dfs, steps, soldepth, path = DFSSearch.dfs(initialstate, goalState)
endtime = time.time()
print("(dfs)" + dfs + " in time " + str("{:.2f}".format((endtime-starttime))) + " seconds and in "
      + str(steps) + " nodes expanded and depth ", soldepth, "and path to goal", path)

starttime = time.time()
A, steps, soldepth= ASearch.A_star(initialstate)
endtime = time.time()
runningtime = endtime - starttime
print("(A*)" + A + " in time " + str("{:.2f}".format(runningtime)) + " seconds and in "
      + str(steps) + " nodes expanded and depth ", soldepth)

