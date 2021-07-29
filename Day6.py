# Day 6 - Advent of code

def processFormInputsAnyoneYes(filename):

    with open(filename) as file:
        lines = file.readlines()

    TotalCount = 0
    charPerGroup = []
    for line in lines:
        if line == '\n':
            TotalCount += len(set(charPerGroup))
            charPerGroup = []
            continue
        else:
            dataLine = line.strip()
            for chars in dataLine:
                charPerGroup.append(chars)

    # Add the information of the last element in the file            
    TotalCount += len(set(charPerGroup))
    return TotalCount


def processFormInputsEveryoneYes(filename):

    with open(filename) as file:
        lines = file.readlines()

    TotalCount = 0
    totalPeopleInGroup = 0
    charPerGroup = {}
    for line in lines:
        if line == '\n':
            for count in charPerGroup.values():
                if count == totalPeopleInGroup:
                    TotalCount += 1
            charPerGroup.clear()
            totalPeopleInGroup = 0
            continue
        else:
            totalPeopleInGroup += 1
            dataLine = line.strip()
            for chars in dataLine:
                if chars in charPerGroup:
                    charPerGroup[chars] += 1
                else:
                    charPerGroup[chars] = 1

    # Add the information of the last element in the file            
    for count in charPerGroup.values():
        if count == totalPeopleInGroup:
            TotalCount += 1

    return TotalCount

print(processFormInputsAnyoneYes('Day6_Input.txt'))
print(processFormInputsEveryoneYes('Day6_Input.txt'))