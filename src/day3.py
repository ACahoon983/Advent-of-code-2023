# creates array of potential parts
def createNumsList(engine):
    numsList = []
    row = 0
    for line in engine:
        column = 0
        while column < len(line):
            if line[column].isdigit():
                number, columnEnd = findNumEnd(line, column)
                numsList.append([number, max(0, row - 1),
                                 min(len(engine), row + 2),
                                 max(0, column - 1),
                                 min(len(line), columnEnd + 2)])
                column = columnEnd
            column += 1
        row += 1
    return numsList


# determines full numbers and bounds to check for symbols
def findNumEnd(line, column):
    number = line[column]
    columnEnd = column
    if line[column + 1].isdigit():
        nextDigit, columnEnd = findNumEnd(line, column + 1)
        number += nextDigit
    return (number, columnEnd)


# determines if numbers are parts
def findParts(numsList, engine):
    partsSum = 0
    starList = []
    for num in numsList:
        dontDuplicate = False
        for row in range(num[1], num[2]):
            for column in range(num[3], num[4]):
                if (not engine[row][column].isdigit()
                        and not engine[row][column] == '.'
                        and not engine[row][column] == '\n'):
                    partNumber = int(num[0])
                    if not dontDuplicate:
                        partsSum += partNumber
                        dontDuplicate = True
                if (engine[row][column] == '*'):
                    starList.append([row, column, int(num[0])])
    return partsSum, starList


# determines if '*' are gears
def findGears(starList):
    gearRatioSum = 0
    gearList = []
    gearList.append(starList[0])
    for star in starList[1:]:
        newPosition = True
        for gear in gearList:
            if star[0] == gear[0] and star[1] == gear[1]:
                gear.append(star[2])
                newPosition = False
        if newPosition:
            gearList.append(star)
    for gear in gearList:
        if len(gear) == 4:
            gearRatioSum += gear[2] * gear[3]
    return gearRatioSum


def part1(filename):
    file = open(filename, 'r')
    engine = file.readlines()
    numsList = createNumsList(engine)
    partsSum, gearList = findParts(numsList, engine)
    return partsSum


def part2(filename):
    file = open(filename, 'r')
    engine = file.readlines()
    numsList = createNumsList(engine)
    sumOfParts, starList = findParts(numsList, engine)
    gearRatioSum = findGears(starList)
    return gearRatioSum


    #rows, cols = (len(engine), len(engine[0]))
    #print([[0 for i in range(cols)] for j in range(rows)])


if __name__ == '__main__':
    print(f'part 1 answer is {part1("input/day3.txt")}')
    print(f'part 2 answer is {part2("input/day3.txt")}')
