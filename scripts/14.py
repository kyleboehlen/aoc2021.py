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
    pairsTrackerTemplate = {}
    pairsTracker = {}
    pairsRules = {}

    # Build rules and OG counts
    for index, line in enumerate(input):
        if index == 0:
            polymerTemplate = line
        elif index > 1:
            parts = line.split(' -> ')
            pairsTrackerTemplate[parts[0]] = 0
            pairsRules[parts[0]] = [parts[0][0] + parts[1], parts[1] + parts[0][1]]

    # Build originally pair counts
    pairsTracker = pairsTrackerTemplate.copy()
    for i in range(0, len(polymerTemplate)):
        if i < len(polymerTemplate) - 1:
            pairsTracker[polymerTemplate[i] + polymerTemplate[i+1]] += 1

    # Do the other 39 steps
    for i in range(40):
        workingPairsTracker = pairsTracker.copy()
        pairsTracker = pairsTrackerTemplate.copy()
        for pair in workingPairsTracker:
            pairsTracker[pairsRules[pair][0]] += int(workingPairsTracker[pair])
            pairsTracker[pairsRules[pair][1]] += int(workingPairsTracker[pair])

    charDict = {}

    for pair in pairsTracker:
        char = pair[0]
        if char not in charDict:
            charDict[char] = 0
        # else:
        charDict[char] += int(pairsTracker[pair])

    # Off by one
    charDict[polymerTemplate[-1]] += 1

    # print(charDict)
    charDict = dict(sorted(charDict.items(), key=lambda item: item[1]))
    for char in charDict:
        if charDict[char] > 0:
            leastCommon = charDict[char]
            break
    mostCommon = charDict[list(charDict.keys())[-1]]
    checksum = mostCommon - leastCommon
    print("Part 2: " + str(checksum))