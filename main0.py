import BFSSearch
import time
import DFSSearch
import random

goalState = "012345678"
initialstate = ''.join(random.sample("012345678", 9))
print("initialstate is ", initialstate)


# Python3 program to check if a given
# instance of 8 puzzle is solvable or not

# Python 3 program to count inversions in an array

def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle):
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])

    # return true if inversion count is even.
    return (inv_count % 2 == 0)


# Driver code
if isSolvable(initialstate):
    print("Solvable")
else:
    print("Not solvable")


starttime = time.time()
(bfs, cost, steps1) = BFSSearch.BFS(initialstate, goalState)
endtime = time.time()
print(bfs)
print(steps1)
print("(BFS) in time " + str(endtime - starttime) + " and in " + str(cost) + " steps")

starttime = time.time()
(dfs, steps) = DFSSearch.dfs(initialstate, goalState)
endtime = time.time()
print("(DFS)" + dfs + " in time " + str(endtime - starttime) + " and in " + str(steps) + " steps")
