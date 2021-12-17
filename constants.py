from classes.day1 import SonarSweep
from classes.day2 import Dive
from classes.day3 import BinaryDiagnostic
from classes.day4 import SquidGames
from classes.day5 import HydrothermalVenture
from classes.day6 import Lanternfish
from classes.day7 import TreacheryOfWhales
from classes.day8 import SegmentSearch
from classes.day9 import SmokeBasin
from classes.day10 import SyntaxScoring

# Location of questions
Files = {
    1: './questions/day1.txt',
    2: './questions/day2.txt',
    3: './questions/day3.txt',
    4: './questions/day4.txt',
    5: './questions/day5.txt',
    6: './questions/day6.txt',
    7: './questions/day7.txt',
    8: './questions/day8.txt',
    9: './questions/day9.txt',
    10: './questions/day10.txt',
}

# Menu
Menu = {
    ' [0] Quit ': 'End Program',
    ' [1] Day 1': 'Sonar Sweep',
    ' [2] Day 2': 'Dive!',
    ' [3] Day 3': 'Binary Diagnostic',
    ' [4] Day 4': 'Giant Squid',
    ' [5] Day 5': 'Hydrothermal Venture',
    ' [6] Day 6': 'Lanternfish',
    ' [7] Day 7': 'The Treacher of Whales',
    ' [8] Day 8': 'Seven Segment Search',
    ' [9] Day 9': 'Smoke Basin',
    '[10] Day 10': 'Syntax Scoring',
}

banner = [
    "***************************",
    "*   Advent of Code 2021   *",
    "***************************"
]


def interface() -> int:
    invalid = True

    for option in Menu:
        print("%s : %s" % (option, Menu.get(option)))

    while(invalid):
        choice = int(input('Select between 0-10: '))
        if(choice < 11 and choice > -1):
            invalid = False
        else:
            print("** invalid selection **")

    return choice


def onQuestion(selection, day) -> None:
    if(selection[0].lower() == 'y'):
        print("")
        with open(Files.get(day), "r") as file:
            lines = [line.strip() for line in file]

        for line in lines:
            print(line)

    return selection


def onSelect(selection) -> object:
    if(selection == 1):
        return SonarSweep()
    if(selection == 2):
        return Dive()
    if(selection == 3):
        return BinaryDiagnostic()
    if(selection == 4):
        return SquidGames()
    if(selection == 5):
        return HydrothermalVenture()
    if(selection == 6):
        return Lanternfish()
    if(selection == 7):
        return TreacheryOfWhales()
    if(selection == 8):
        return SegmentSearch()
    if(selection == 9):
        return SmokeBasin()
    if(selection == 10):
        return SyntaxScoring()
