class SonarSweep:
    def __init__(self) -> None:
        filepath = "./classes/assets/day1/input.txt"
        self.input = list(
            map(int, self.scanFile(filepath)))
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            readings = [line.strip() for line in file]
        return readings

    def part1(self) -> int:
        """
        Using 2 pointers, this method traverses the list in one pass by checking if pointer 1 < pointer 2
        Runtime complexity: O(n)
        """
        i = 0
        increased = 0
        decreased = 0
        same = 0

        while i < len(self.input)-1:
            j = i+1
            if(self.input[i] < self.input[j]):
                increased += 1
            if(self.input[i] > self.input[j]):
                decreased += 1
            if(self.input[i] == self.input[j]):
                same += 1
            i += 1

        return increased

    def part2(self) -> int:
        """
        Using 3 pointers, this method traverses the list in one pass by checking if the sum created by the first
        3 pointers list[i] + list[j] + list[k] < the sum created by the next 3 pointers list[i+1] + list[j+1] + list[k+1]
        Runtime complexity: O(n)
        """
        i = 0
        increased = 0
        decreased = 0
        same = 0

        while i < len(self.input)-3:
            j = i+1
            k = i+2
            sum1 = self.input[i] + self.input[j] + self.input[k]
            sum2 = self.input[i+1] + \
                self.input[j+1] + self.input[k+1]
            if(sum1 < sum2):
                increased += 1
            if(sum1 > sum2):
                decreased += 1
            if(sum1 == sum2):
                same += 1
            i += 1
        return increased

    def solution(self) -> None:
        print("")
        day = "**** Day 1: Sonar Sweep ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
