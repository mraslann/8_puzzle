import random
import Tree

# generating random string with 9 digits to represent all tiles ( 0 for empty tile )
initialState = ''.join(random.sample("012345678", 9))
print(initialState)
goalState = "123456780"
root = None

def converttostring(current):
    # initialize an empty string
    str = ""

    # traverse in the string
    for i in current:
        str += i

        # return string
    return str
# function to get the posistion of an element in the state
def getpos(currentstate, element):
    for i in currentstate:
        if element == i:
            return (currentstate.index(i))


def generatepossiblestates(currentstate):
    possiblestates = []
    position = getpos(currentstate, "0")
    if position == 4:
        j = 1
        for i in range(0, 4):
            current = list(currentstate)
            current[j], current[4] = current[4], current[j]
            current = converttostring(current)
            possiblestates.append(current)
            j = j + 2
        print(possiblestates)
    else:
        if position == 0:
            j = 1
            for i in range(0, 2):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                j = j + 3
            print(possiblestates)
        if position == 1:
            j = 0
            for i in range(0, 3):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                j = j + 2
            print(possiblestates)
        if position == 2:
            j = 1
            for i in range(0, 2):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                j = j + 4
            print(possiblestates)

        if position == 3:
            j = 0
            for i in range(0, 3):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                if j == 0:
                    j = 4
                else:
                    j = j+2
            print(possiblestates)

        if position == 5:
            j = 2
            for i in range(0, 3):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                if j == 4:
                    j = j + 4
                else:
                    j = j + 2
            print(possiblestates)
        if position == 6:
            j = 3
            for i in range(0, 2):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                j = j + 4
            print(possiblestates)

        if position == 7:
            j = 4
            for i in range(0, 3):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                j = j + 2
            print(possiblestates)

        if position == 8:
            j = 5
            for i in range(0, 2):
                current = list(currentstate)
                current[j], current[position] = current[position], current[j]
                current = converttostring(current)
                possiblestates.append(current)
                j = j + 2
            print(possiblestates)

generatepossiblestates(initialState)
