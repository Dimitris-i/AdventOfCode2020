# Day 5 - Advent of code

def findSeatID(seatString):

    if len(seatString) < 10:
        return None

    rows = range(0,128)
    columns = range(0,8)

    for char in seatString:
        middleRow = int(len(rows)/2)
        middleColumn = int(len(columns)/2)
        if (char == 'F'):
            rows = rows[:middleRow]
        elif (char == 'B'):
            rows = rows[middleRow:]
        elif (char == 'L'):
            columns = columns[:middleColumn]
        elif (char == 'R'):
            columns = columns[middleColumn:]
        
    return rows[0] * 8 + columns[0]

def findSeatIDRec(seatString, rowRange, columnRange):

    if len(seatString) < 10:
        return None

    row = findSeatRow(seatString[:7], rowRange)
    column = findSeatColumn(seatString[7:], columnRange)

    return row[0] * 8 + column[0]

def findSeatRow(seatString, rows):

    if len(rows) == 1:
        return rows

    if (seatString[0] == 'F'):
        rows = findSeatRow(seatString[1:], rows[:int(len(rows)/2)])
    elif (seatString[0] == 'B'):
        rows = findSeatRow(seatString[1:], rows[int(len(rows)/2):])

    return rows

def findSeatColumn(seatString, columns):

    if len(columns) == 1:
        return columns

    if (seatString[0] == 'L'):
        columns = findSeatColumn(seatString[1:], columns[:int(len(columns)/2)])
    elif (seatString[0] == 'R'):
        columns = findSeatColumn(seatString[1:], columns[int(len(columns)/2):])

    return columns

def readTickesAndFindSeatIds(filename, rowRange, columnRange):
    
    tickets = readInput(filename)
    
    seatsID = []

    for seatString in tickets:
        seatsID.append(findSeatIDRec(seatString[:-1], rowRange, columnRange))

    return seatsID[:-1]

def findMaxSeatId(filename, rowRange, columnRange):

    return max(readTickesAndFindSeatIds(filename, rowRange, columnRange))

def findMySeatID(filename, rowRange, columnRange):

    seat_ids = readTickesAndFindSeatIds(filename, rowRange, columnRange)
    seat_ids.sort()

    shifted_seat_ids = seat_ids[1:] + [seat_ids[-1] + 1]
    diffs = list(map(lambda tup: tup[0] - tup[1], zip(shifted_seat_ids, seat_ids)))
    findPointDiffs = [i for i in range(0, len(diffs)) if diffs[i] == 2 ]
    seat_before_missing = seat_ids[max(findPointDiffs)]
    return seat_before_missing + 1


def readInput(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


print(findMaxSeatId('Day5_input.txt',range(0,128),range(0,8)))
print(findMySeatID('Day5_input.txt',range(0,128),range(0,8)))