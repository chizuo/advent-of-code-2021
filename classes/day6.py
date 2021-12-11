import copy


class Lanternfish:
    def __init__(self) -> None:
        filepath = "./classes/assets/day6/input.txt"
        self.input = self.scanFile(filepath)
        self.part1solution = self.sim(80)
        self.part2solution = self.sim(256)

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            line = file.readline()
            count = 0
            number = ''  # string to build the integers from the text file parser
            lanternfish = []  # A list, where each element represents a Lantern Fish, and the value representing its stage in pregnancy

            for char in line:
                if(char == ','):
                    lanternfish.append(int(number))
                    number = ''
                if(char.isdigit()):
                    number += char
                    if(count == len(line)-1):
                        lanternfish.append(int(number))
                count += 1

        group = []

        for i in range(9):  # 9 to represent all possible numbers that'll exist in the group: 0 -> 8
            group.append(lanternfish.count(i))

        return group

    def sim(self, days):
        """
        Description: Using the initial occurences of a particular fish start state, this method creates an
        abstract queue to increment the amount of children each group will have after each day.
        """
        group = copy.deepcopy(self.input)

        for i in range(days):
            # this group of fish just gave birth so remove them from the front of the queue
            thisGroup = group.pop(0)

            # add them to the 7th day, element 6 post pop, to reset birthing cycle
            group[6] += thisGroup

            # this group of fish would have made 1 child each
            # therefore, add that same number to the end of the list, representing 8 days til it can give birth
            group.append(thisGroup)

        population = 0

        for thisGroup in group:
            population += thisGroup

        return population

    def solution(self) -> None:
        print("\n**** Day 6: Lanternfish ****")
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
