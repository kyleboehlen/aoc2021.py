# import numpy as py

def solvePuzzle(input):
    array = []
    for i in input:
        array.append(list(i))

    risk = 0
    numLines = len(array)
    for y, line in enumerate(array):
        for x, value in enumerate(line):
            lessThan = True
            intValue = int(value)

            if x > 0:
                if intValue >= int(line[x-1]):
                    lessThan = False
            
            if x < len(line) - 1:
                if intValue >= int(line[x+1]):
                    lessThan = False

            if y > 0:
                if intValue >= int(array[y-1][x]):
                    lessThan = False

            if y < numLines - 1:
                if intValue >= int(array[y+1][x]):
                    lessThan = False
            
            if lessThan:
                risk += intValue + 1

    print("Part one: " + str(risk))
