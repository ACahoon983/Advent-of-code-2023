import re


def part1(filename):
    file = open(filename, 'r')
    gameData = file.readlines()
    sumOfGameIDs = 0
    for game in gameData:
        gameInfo = re.split(':|,|;', game)
        gameID = 0
        for pulls in gameInfo:
            info = pulls.split()
            if info[0] == 'Game':
                gameID = int(info[1])
            else:
                cubes = int(info[0])
                if ((cubes > 14 and info[1] == 'blue')
                        or (cubes > 13 and info[1] == 'green')
                        or (cubes > 12 and info[1] == 'red')):
                    sumOfGameIDs -= gameID
                    break
        sumOfGameIDs += gameID
    return sumOfGameIDs


def part2(filename):
    file = open(filename, 'r')
    gameData = file.readlines()
    cubePowerSum = 0
    for game in gameData:
        blueCubes = 0
        greenCubes = 0
        redCubes = 0
        gameInfo = re.split(':|,|;', game)
        for pulls in gameInfo:
            info = pulls.split()
            if info[1] == 'blue':
                blueCubes = max(blueCubes, int(info[0]))
            elif info[1] == 'green':
                greenCubes = max(greenCubes, int(info[0]))
            elif info[1] == 'red':
                redCubes = max(redCubes, int(info[0]))
        cubePowerSum += blueCubes * greenCubes * redCubes
    return cubePowerSum


if __name__ == '__main__':
    print(f'part 1 answer is {part1("input/day2.txt")}')
    print(f'part 2 answer is {part2("input/day2.txt")}')
