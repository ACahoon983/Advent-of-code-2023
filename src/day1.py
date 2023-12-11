def part1(filename):
    file = open(filename, 'r')
    calibrationStrings = file.readlines()
    calibrationSum = 0
    value1 = None
    value2 = 0
    for calibrationLine in calibrationStrings:
        for character in calibrationLine:
            if value1 == None:
                if character.isdigit():
                  value1 = int(character)
            else:
                if character.isdigit():
                    value2 = int(character)
        calibrationSum += value1 * 10 + value2
    return calibrationSum

        