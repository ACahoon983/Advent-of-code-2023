def convertString(line):
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7even")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")
    return line

def part1(filename):
    file = open(filename, 'r')
    calibrationStrings = file.readlines()
    calibrationSum = 0
    value1 = 0
    value2 = 0
    for calibrationLine in calibrationStrings:
        value1 = None
        for character in calibrationLine:
            if value1 is None:
                if character.isdigit():
                    value1 = int(character)
                    value2 = value1
            else:
                if character.isdigit():
                    value2 = int(character)
        calibrationSum += value1 * 10 + value2
    file.close
    return calibrationSum

def part2(filename):
    file = open(filename, 'r')
    calibrationStrings = file.readlines()
    calibrationSum = 0
    value1 = 0
    value2 = 0
    for calibrationLine in calibrationStrings:
        convertedLine = convertString(calibrationLine)
        value1 = None
        for character in convertedLine:
            if value1 is None:
                if character.isdigit():
                    value1 = int(character)
                    value2 = value1
            else:
                if character.isdigit():
                    value2 = int(character)
        calibrationSum += value1 * 10 + value2
    file.close
    return calibrationSum


if __name__ == '__main__':
    print(f'part 1 answer is {part1("input/day1.txt")}')
    print(f'part 2 answer is {part2("input/day1.txt")}')
