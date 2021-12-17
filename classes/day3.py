import copy


class BinaryDiagnostic:
    def __init__(self) -> None:
        filepath = "./classes/assets/day3/input.txt"
        self.input = self.scanFile(filepath)
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            readings = [line.strip() for line in file]
        return readings

    def part1(self) -> int:
        """

        """
        def binaryToDecimal(binary) -> int:
            """

            """
            bit = 0
            decimal = 0
            power = len(binary)-1

            while(bit < len(binary)):
                decimal += int(binary[bit])*(2**(power-bit))
                bit += 1

            return decimal

        bit = 0
        deltaRate = ""
        gammaRate = ""

        #
        while(bit < len(self.input[0])):
            #
            row = 0
            gamma = 0
            delta = 0

            # Inner loop parses each bit in binary to check if that column falls under gamma or delta
            while(row < len(self.input)):
                binary = self.input[row]

                if(int(binary[bit]) == 1):
                    gamma += 1
                else:
                    delta += 1

                row += 1

            # Builds the binary for gamma and delta rate
            if(gamma > delta):
                gammaRate += "1"
                deltaRate += "0"
            else:
                gammaRate += "0"
                deltaRate += "1"

            bit += 1

        self.day3gammaRate = gammaRate
        self.day3deltaRate = deltaRate

        return (binaryToDecimal(gammaRate)*binaryToDecimal(deltaRate))

    def part2(self) -> int:
        """
        """
        def binaryToDecimal(binary) -> int:
            """

            """
            bit = 0
            decimal = 0
            power = len(binary)-1

            while(bit < len(binary)):
                decimal += int(binary[bit])*(2**(power-bit))
                bit += 1

            return decimal

        oxygenLog = copy.deepcopy(self.input)
        co2Log = copy.deepcopy(self.input)
        bit = 0

        while(len(oxygenLog) > 1):
            zero = 0
            one = 0

            for log in oxygenLog:
                if(log[bit] == "1"):
                    one += 1
                else:
                    zero += 1

            mcv = "1" if one >= zero else "0"
            newLog = []

            for log in oxygenLog:
                if(log[bit] == mcv):
                    newLog.append(log)

            oxygenLog = copy.deepcopy(newLog)
            bit += 1

        bit = 0
        while(len(co2Log) > 1):
            zero = 0
            one = 0

            for log in co2Log:
                if(log[bit] == "1"):
                    one += 1
                else:
                    zero += 1

            lcv = "0" if one >= zero else "1"
            newLog = []

            for log in co2Log:
                if(log[bit] == lcv):
                    newLog.append(log)

            co2Log = copy.deepcopy(newLog)
            bit += 1

        return (binaryToDecimal(oxygenLog[0])*binaryToDecimal(co2Log[0]))

    def prompt(self) -> None:
        print(self.question)

    def solution(self) -> None:
        print("")
        day = "**** Day 3: Binary Diagnostic ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
