import BFSSearch
import time
import DFSSearch
import random


goalState = "012345678"
# initialstate = ''.join(random.sample("012345678", 9))
initialstate="413270568"
print("initialstate is ", initialstate)
# Python3 program to check if a given
# instance of 8 puzzle is solvable or not

# Python 3 program to count inversions in an array

# Function to Use Inversion Count
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


# This Function will use MergeSort to count inversions

def _mergeSort(arr, temp_arr, left, right):
    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right) // 2

        # It will calculate inversion
        # counts in the left subarray

        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)

        # It will calculate inversion
        # counts in right subarray

        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


# This code is contributed by ankush_953


# A utility function to count
# inversions in given array 'arr[]'

# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(initialstate):
    puzzle = list(initialstate)
    inv_count = mergeSort(puzzle, len(puzzle))

    # return true if inversion count is even.
    return (inv_count % 2 == 0)


# Driver code
if (isSolvable(initialstate)):
    print("not Solvable")
    # exit()
else:
    print("Solvable")

starttime = time.time()
(bfs, steps1) = BFSSearch.BFS(initialstate, goalState)
endtime = time.time()
print("(BFS)" + bfs + " in time " + str(endtime-starttime) + " and in " + str(steps1) + " steps")

starttime = time.time()
(dfs, steps) = DFSSearch.dfs(initialstate, goalState)
endtime = time.time()
print("(DFS)" + dfs + " in time " + str(endtime-starttime) + " and in " + str(steps) + " steps")