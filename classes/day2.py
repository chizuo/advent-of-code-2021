class Dive:
    def __init__(self) -> None:
        filepath = "./classes/assets/day2/input.txt"
        self.input = self.scanFile(filepath)
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            readings = [line.strip() for line in file]
        return readings

    def part1(self) -> int:
        """
        This method traverses the list of inputs, which are strings composed of a command and an integer.
        For each entry in the list, the string contained in the entry is parsed and split where a space is found,
        since we know it contains the pattern "<string> <int>". The 2 are parsed per pass to determine if this
        entry will add to the forward total and depth.
        Runtime complexity: O(n)
        """
        forward = 0
        depth = 0

        for entry in self.input:
            parsed = entry.split()
            parsed[1] = int(parsed[1])

            if(parsed[0] == 'up'):
                depth -= parsed[1]

            if(parsed[0] == 'down'):
                depth += parsed[1]

            if(parsed[0] == 'forward'):
                forward += parsed[1]

        return depth * forward

    def part2(self) -> int:
        """
        This method traverses the list of inputs, which are strings composed of a command and an integer.
        For each entry in the list, the string contained in the entry is parsed and split where a space is found,
        since we know it contains the pattern "<string> <int>". The 2 are parsed per pass to determine if this
        entry will add to the forward total, aim, and depth.
        Runtime complexity: O(n)
        """
        aim = 0
        forward = 0
        depth = 0

        for entry in self.input:
            parsed = entry.split()
            parsed[1] = int(parsed[1])
            thisForward = 0

            if(parsed[0] == 'up'):
                aim -= parsed[1]

            if(parsed[0] == 'down'):
                aim += parsed[1]

            if(parsed[0] == 'forward'):
                thisForward = parsed[1]
                forward += thisForward
            depth += aim * thisForward

        return depth * forward

    def solution(self) -> None:
        print("")
        day = "**** Day 2: Dive! ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
