

def solvePuzzle(input):
    polymerTemplate = ''
    pairsDict = {}

    for index, line in enumerate(input):
        if index == 0:
            polymerTemplate = line
        elif index > 1:
            parts = line.split(' -> ')
            pairsDict[parts[0]] = parts[1]
    
    nextPolymer = ''
    for step in range(10):
        for i in range(0, len(polymerTemplate)):
            if i < len(polymerTemplate) - 1:
                dictValue = pairsDict[polymerTemplate[i] + polymerTemplate[i+1]]
            else:
                dictValue = ''
            nextPolymer += polymerTemplate[i] + dictValue
    
        polymerTemplate = nextPolymer
        nextPolymer = ''
    
    charDict = {}
    for char in polymerTemplate:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    
    charDict = dict(sorted(charDict.items(), key=lambda item: item[1]))
    leastCommon = charDict[list(charDict.keys())[0]]
    mostCommon = charDict[list(charDict.keys())[-1]]
    checksum = mostCommon - leastCommon
    print("Part 1: " + str(checksum))