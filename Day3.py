# Day 3 - Advent of Code

def readInputFile(fileName):
    with open(filename) as f:
        content = f.readlines()
        # Remove the new line characters
        content = [line[:-1] for line in content]
    return content

def findNumberOfTrees(travelMap, rightOffset, downOffset):
    if not travelMap:
        return 0

    numOfTrees = 0
    currentRow = 0
    currentColumn = 0
    foldLengh = len(travelMap[0])
    finishRow = len(travelMap)

    while currentRow < finishRow:
        currentRow += downOffset
        currentColumn += rightOffset
        if currentColumn >= foldLengh:
            currentColumn = currentColumn - foldLengh
        
        if currentRow >= finishRow:
            break

        if travelMap[currentRow][currentColumn] == '#':
            numOfTrees += 1
    
    return numOfTrees

filename = 'Day3_input.txt'
travelMap = readInputFile(filename)
offsets = [(1,1), (3,1), (5,1), (7,1), (1,2)]
totalNumberOfMultTrees = 1
for offset in offsets:
    totalNumberOfMultTrees *= findNumberOfTrees(travelMap, offset[0], offset[1])

print(totalNumberOfMultTrees)

