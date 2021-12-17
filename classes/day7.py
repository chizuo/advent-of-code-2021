from classes.assets.day7.constants import infinite


class TreacheryOfWhales:
    def __init__(self) -> None:
        filepath = "./classes/assets/day7/input.txt"
        self.input = self.scanFile(filepath)
        self.part1solution = self.calculateFuel(1)
        self.part2solution = self.calculateFuel(2)

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            line = file.readline()

        return list(map(int, line.split(',')))

    def calculateFuel(self, part) -> None:
        def checkFuel(crabs, location, crabDict, part) -> int:
            fuel = 0
            for crab in crabs:
                if(part == 1):
                    fuel += abs(location - crab)*crabDict[crab]
                else:
                    steps = abs(location - crab)
                    stepsFuel = 0
                    for i in range(1, steps+1):
                        stepsFuel += i
                    fuel += stepsFuel*crabDict[crab]

            return fuel

        crabs = self.input
        crab_locations = set(crabs)
        crab_count = {}
        xmax = max(self.input)
        for location in crab_locations:
            crab_count[location] = crabs.count(location)

        sortCount = dict(
            sorted(crab_count.items(), key=lambda x: x[1], reverse=True))

        keys = sortCount.keys()
        lowest = infinite

        for key in keys:
            current = key
            currentKeyFuel = checkFuel(
                crab_locations, current, crab_count, part)

            if(lowest >= currentKeyFuel):
                lowest = currentKeyFuel
                # check if we are at xmax
                if(current == xmax):
                    continue
                # if not, check its neighbors +1 until slope increases
                while(True):
                    nextFuel = checkFuel(
                        crab_locations, current+1, crab_count, part)
                    if(lowest > nextFuel):
                        lowest = nextFuel
                        current += 1
                        if(current == xmax):
                            break
                    else:
                        break

                current = key

                # check if we are at xmin
                if(current == 0):
                    continue
                # if not, check its neighbords -1 until slope increases
                while(True):
                    nextFuel = checkFuel(
                        crab_locations, current-1, crab_count, part)
                    if(lowest > nextFuel):
                        lowest = nextFuel
                        current -= 1
                        if(current == 0):
                            break
                    else:
                        break

        return lowest

    def solution(self) -> None:
        print("")
        day = "**** Day 7: The Treachery of Whales ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
