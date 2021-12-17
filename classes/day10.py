from classes.assets.day10.constant import lexeme, rubric_p1, rubric_p2


class SyntaxScoring:
    def __init__(self) -> None:
        filepath = "./classes/assets/day10/input.txt"
        self.input = self.scanFile(filepath)
        self.part1solution = self.part1(lexeme.keys())
        self.part2solution = self.part2(lexeme.keys())

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            lines = [line.strip() for line in file]

        return lines

    def part1(self, keys) -> int:
        score = 0

        for string in self.input:
            stack = []
            for char in string:
                if(char in keys):
                    stack.append(lexeme.get(char))
                else:
                    lex = stack.pop()
                    if(lex != char):
                        score += rubric_p1.get(char)
                        break

        return score

    def part2(self, keys) -> int:
        scores = []

        for string in self.input:
            stack = []
            corrupted = False
            for char in string:
                if(char in keys):
                    stack.append(lexeme.get(char))
                else:
                    lex = stack.pop()
                    if(lex != char):
                        corrupted = True
                        break

            if(not corrupted):
                score = 0
                while(stack):
                    score *= 5
                    score += rubric_p2.get(stack.pop())
                scores.append(score)

        scores.sort()
        return scores[int(len(scores)/2)]

    def solution(self) -> None:
        print("")
        day = "**** Day 10: Syntax Scoring ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
