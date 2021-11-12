import DFSSearch
import time
import random
import BFSSearch


goalState = "012345678"
initialstate = ''.join(random.sample("012345678", 9))
print("initialstate is ", initialstate)
initialstate = "125034678"
starttime = time.time()
dfs, steps, soldepth, path = BFSSearch.BFS(initialstate, goalState)
endtime = time.time()
print("(bfs)" + dfs + " in time " + str("{:.2f}".format((endtime-starttime))) + " seconds and in "
      + str(steps) + " steps and depth ", soldepth, "and path to goal", path)

starttime = time.time()
dfs, steps, soldepth, path = DFSSearch.dfs(initialstate, goalState)
endtime = time.time()
print("(dfs)" + dfs + " in time " + str("{:.2f}".format((endtime-starttime))) + " seconds and in "
      + str(steps) + " steps and depth ", soldepth, "and path to goal", path)

# print(cProfile.run("main()"))
