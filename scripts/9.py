# import numpy as py

def solvePuzzle(input):
    array = []
    cords = []
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
                cords.append(str(x) + ',' + str(y))
                lineLen = len(line)

    print("Part one: " + str(risk))

    basinSizes = []
    visitedCords = [[0] * lineLen for i in range(numLines)]
    for cord in cords:
        x = int(cord.split(',')[0])
        y = int(cord.split(',')[1])
        basinSize = getBasinSize(array, x, y, lineLen, numLines, visitedCords, 0)
        basinSizes.append(basinSize)

    basinSizes.sort()
    basinSizes.reverse()
    basinTotal = basinSizes[0] * basinSizes[1] * basinSizes[2]

    print("Part two: " + str(basinTotal))

def getBasinSize(array, x, y, len, num, visitedCords, count):
    if visitedCords[y][x] == 0:
        visitedCords[y][x] = 1
        count = 1
    else:
        return 0
    
    if x > 0:
        if int(array[y][x-1]) != 9:
            count += getBasinSize(array, x-1, y, len, num, visitedCords, count)
    
    if x < len - 1:
        if int(array[y][x+1]) != 9:
            count += getBasinSize(array, x+1, y, len, num, visitedCords, count)

    if y > 0:
        if int(array[y-1][x]) != 9:
            count += getBasinSize(array, x, y-1, len, num, visitedCords, count)

    if y < num - 1:
        if int(array[y+1][x]) != 9:
            count += getBasinSize(array, x, y+1, len, num, visitedCords, count)

    return count
