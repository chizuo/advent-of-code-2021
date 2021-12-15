class SegmentSearch:
    def __init__(self) -> None:
        filepath = "./classes/assets/day8/input.txt"
        self.input1 = self.scanFile1(filepath)
        self.input2 = self.scanFile2(filepath)
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile1(self, loc) -> list:
        with open(loc, "r") as file:
            lines = [line.strip() for line in file]

        output = []

        for line in lines:
            start = line.find('|')+1
            thisString = line[start:len(line)]
            output.append(thisString.split())

        return output

    def scanFile2(self, loc) -> list:
        with open(loc, "r") as file:
            lines = [line.strip() for line in file]

        output = []

        for line in lines:
            output.append(line.split())

        return output

    def part1(self) -> int:
        instance = 0

        for entry in self.input1:
            for signal in entry:
                # string is number 1
                if(len(signal) == 2):
                    instance += 1
                # string is number 4
                if(len(signal) == 4):
                    instance += 1
                # string is number 7
                if(len(signal) == 3):
                    instance += 1
                # string is number 8
                if(len(signal) == 7):
                    instance += 1

        return instance

    def part2(self) -> int:
        def decode_1478(size) -> dict:
            if(size == 2):
                return 1
            if(size == 4):
                return 4
            if(size == 3):
                return 7
            if(size == 7):
                return 8
            return decoder

        def decode_690(decoder, signal) -> int:
            # if 1 is in the decoder and 1 is not a subset of the signal, the signal is 6
            if(1 in decoder and not decoder[1].issubset(signal)):
                return 6

            # 4 is in the decoder and 4 is a subset of the signal, the signal is 9
            if(4 in decoder and decoder[4].issubset(signal)):
                return 9

            # if 1 and 4 are in the decoder, but neither is a subset of the signal the signal is 0
            if(1 in decoder and 4 in decoder):
                return 0

            # not enough information to in the decoder to deduce the signal
            return -1

        def decode_235(decoder, signal) -> int:
            # if 1 is in the decoder and 1 is a subset of this signal, the signal is 3
            if(1 in decoder and decoder[1].issubset(signal)):
                return 3

            # if 1 is in the decoder but 1 is not a subset of this signal and
            # 9 is in the decoder and the signal is a subset of 9, the signal is 5
            if(9 in decoder and signal.issubset(decoder[9])):
                return 5

            # if 1 and 9 are in the decoder but this signal is neither 1 or 9, the signal is 2
            if(1 in decoder and 9 in decoder):
                return 2

            # not enough information to in the decoder to deduce the signal
            return -1

        # added to this method for clarity and context
        output = self.input1
        values = []
        count = 0

        for entry in self.input2:
            decoder = {}
            number = ''

            while(len(entry) > 0):
                thisSignal = entry.pop(0)
                size = len(thisSignal)

                if(thisSignal == '|'):
                    continue

                # this signal must be either 1,4,7 or 8
                if(size == 2 or size == 4 or size == 3 or size == 7):
                    response = decode_1478(size)

                # this signal must be either 6,9 or 0
                if(size == 6):
                    response = decode_690(decoder, set(thisSignal))

                # this signal must be either 2,3 or 5
                if(size == 5):
                    response = decode_235(decoder, set(thisSignal))

                if(response != -1):
                    decoder[response] = set(thisSignal)
                else:  # add back to the queue until the decoder has enough to deduce this signal
                    entry.append(thisSignal)

            for entry in output[count]:
                size = len(entry)

                if(size == 5):
                    number += str(decode_235(decoder, set(entry)))
                elif(size == 6):
                    number += str(decode_690(decoder, set(entry)))
                else:
                    number += str(decode_1478(size))

            values.append(int(number))
            count += 1
        return sum(values)

    def solution(self) -> None:
        print("\n**** Day 8: Seven Segment Search ****", end="\n")
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
