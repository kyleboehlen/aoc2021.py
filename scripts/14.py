globalCharDict = {}
globalPairsDict = {}

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

    # Let's try again
    polymerTemplate = ''

    for index, line in enumerate(input):
        if index == 0:
            polymerTemplate = line
        elif index > 1:
            parts = line.split(' -> ')
            globalPairsDict[parts[0]] = parts[1]

    # We'll built it first so we don't have to check keys over and over again
    for insert in globalPairsDict:
        if globalPairsDict[insert] not in globalCharDict:
            globalCharDict[globalPairsDict[insert]] = 0

    for i in range(0, len(polymerTemplate)):
        globalCharDict[polymerTemplate[i]] += 1
        if i < len(polymerTemplate) - 1:
            polymerFunc(polymerTemplate[i] + polymerTemplate[i+1], 1)
    
    charDict = dict(sorted(globalCharDict.items(), key=lambda item: item[1]))
    leastCommon = charDict[list(charDict.keys())[0]]
    mostCommon = charDict[list(charDict.keys())[-1]]
    checksum = mostCommon - leastCommon
    print("Part 1 Cleaner: " + str(checksum))

def polymerFunc(pair, count):
    insert = globalPairsDict[pair]
    globalCharDict[insert] += 1
    if count < 10:
        polymerFunc(pair[0] + insert, count + 1)
        polymerFunc(insert + pair[1], count + 1)