import re

def solvePuzzle(input):
    # Set up data structure for storing the boards and numbers
    boardNums = {}
    boards = {} 
    boardCount = -1
    y = 0
    for index, line in enumerate(input):
        if index == 0:
            inputNums = line.split(",")
            continue

        if len(line) <= 1:
            y = 0
            boardCount += 1
            boardNums[boardCount] = []
            continue

        formattedLine = line.strip()
        formattedLine = re.sub(r"\s+", ",", formattedLine)
        for x, num in enumerate(formattedLine.split(',')):
            inputArray = [boardCount, x, y]
            if num not in boards:
                boards[num] = []
            boards[num].append(inputArray)
            boardNums[boardCount].append(num)
        y += 1

    markedNums = []
    boardsWon = []
    boardTracker = {}
    firstChecksumFound = False
    secondChecksumFound = False
    for num in inputNums:
        if firstChecksumFound and secondChecksumFound:
            break
        markedNums.append(num)
        for b in boards[num]:
            if b[0] not in boardTracker:
                boardTracker[b[0]] = [[0] * 5, [0] * 5]
            boardTracker[b[0]][0][b[1]] += 1
            boardTracker[b[0]][1][b[2]] += 1
            if boardTracker[b[0]][0][b[1]] == 5 or boardTracker[b[0]][1][b[2]] == 5:
                # Part 1
                if not firstChecksumFound:
                    checksum = 0
                    for bNum in boardNums[b[0]]:
                        if bNum not in markedNums:
                            checksum += int(bNum)
                    checksum *= int(num)
                    print("Part One: " + str(checksum))
                    firstChecksumFound = True
                # Part 2
                if b[0] not in boardsWon:
                    boardsWon.append(b[0])
                if len(boardsWon) == len(boardNums):
                    checksum = 0
                    for bNum in boardNums[b[0]]:
                        if bNum not in markedNums:
                            checksum += int(bNum)
                    checksum *= int(num)
                    print("Part Two: " + str(checksum))
                    secondChecksumFound = True
                    break
    


    
