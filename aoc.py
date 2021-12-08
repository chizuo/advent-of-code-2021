from classes.day1 import SonarSweep
from classes.day2 import Dive
from classes.day3 import BinaryDiagnostic
from classes.day4 import SquidGames
from classes.day5 import HydrothermalVenture


def main():
    firstDay = SonarSweep()
    firstDay.solution()
    secondDay = Dive()
    secondDay.solution()
    thirdDay = BinaryDiagnostic()
    thirdDay.solution()
    fourthDay = SquidGames()
    fourthDay.solution()
    fifthDay = HydrothermalVenture()
    fifthDay.solution()


main()