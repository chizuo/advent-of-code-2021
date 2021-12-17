import copy


class SquidGames:
    def __init__(self) -> None:
        filepath = "./classes/assets/day4/input.txt"
        self.dicedraw = self.scanFile4BingoDraw(filepath)
        self.board = self.scanFile4Boards(filepath)
        self.bingoboard = self.buildBingoBoards()
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile4BingoDraw(self, loc) -> list:
        with open(loc, "r") as file:
            number = ''
            diceorder = []
            line = file.readline()

            for char in line:
                if(char.isdigit()):
                    number += char
                else:
                    diceorder.append(int(number))
                    number = ''

        return diceorder

    def scanFile4Boards(self, loc) -> list:
        with open(loc, "r") as file:
            # a list of boards in the game
            bingoboard = []
            # a list of rows for a board
            board = []

            rownumber = 1
            number = ''

            for line in file:
                if(len(line) == 15 or len(line) == 14):  # len == 14 is for EOF
                    # a list of numbers for this row of a board
                    row = []
                    for char in line:
                        if(char.isdigit()):  # builds the number
                            number += char
                        # if the character is a space & length of the number is 0, the upcoming digit < 10
                        elif(char.isspace() and len(number) == 0):
                            continue
                        else:  # character in file isn't a number, add number to row of numbers and re-initialize number
                            row.append(int(number))
                            number = ''

                    if(len(line) == 14):  # append final number to the final row of the board in the file
                        row.append(int(number))

                    board.append(row)
                    rownumber += 1

                    if(rownumber == 6):  # a board of 5 rows has been built, add that board to the list of bingo boards and re-initialized board list to empty
                        rownumber = 1
                        bingoboard.append(board)
                        board = []

        return bingoboard

    def buildSet(self, board) -> list:
        row = 0
        boardSets = []
        setColumn1 = set()
        setColumn2 = set()
        setColumn3 = set()
        setColumn4 = set()
        setColumn5 = set()

        while(row < 5):
            column = 0
            rowSet = set()

            while(column < 5):
                if(column == 0):
                    setColumn1.add(board[row][0])

                if(column == 1):
                    setColumn2.add(board[row][1])

                if(column == 2):
                    setColumn3.add(board[row][2])

                if(column == 3):
                    setColumn4.add(board[row][3])

                if(column == 4):
                    setColumn5.add(board[row][4])

                rowSet.add(board[row][column])
                column += 1

            boardSets.append(rowSet)
            row += 1

        boardSets.append(setColumn1)
        boardSets.append(setColumn2)
        boardSets.append(setColumn3)
        boardSets.append(setColumn4)
        boardSets.append(setColumn5)

        return boardSets

    def buildBingoBoards(self) -> list:
        bingoBoards = []
        for board in self.board:
            bingoBoards.append(self.buildSet(board))

        return bingoBoards

    def calcSolution(self, drawn, board, ball):
        """
        Description: method to calculate the answer when bingo is found.
        Accepts: set that represents balls drawn in bingo game, 
                 list of sets that contain all bingo lines of the winning board, 
                 and integer representing the winning ball
        Returns: integer representing the final score
        """
        combineSets = set().union(*board)
        unmarkedSum = 0

        for number in combineSets:
            if(number in drawn):
                continue
            else:
                unmarkedSum += number

        return unmarkedSum*ball

    def part1(self) -> int:
        """
        """
        drawn = set()

        for ball in self.dicedraw:
            drawn.add(ball)

            if(len(drawn) > 4):  # Until we have more than 4 balls drawn, bingo is impossible
                for board in self.bingoboard:
                    for bingoLine in board:
                        if(bingoLine.issubset(drawn)):
                            return self.calcSolution(drawn, board, ball)

    def part2(self) -> int:
        """

        """
        drawn = set()
        remainingBoards = copy.deepcopy(self.bingoboard)
        finalBall = False

        for ball in self.dicedraw:
            # if the remaining boards is 1 and the finalBall has been found, we found the last board and winning ball. Calculate the results
            if(len(remainingBoards) == 1 and finalBall == True):
                return self.calcSolution(drawn, remainingBoards.pop(), winningBall)

            drawn.add(ball)
            bingoboard = copy.deepcopy(remainingBoards)

            if(len(drawn) > 4):  # Until we have more than 4 balls drawn, bingo is impossible
                for board in bingoboard:
                    for bingoLine in board:
                        if(ball in bingoLine):  # optimization before checking issubset
                            if(bingoLine.issubset(drawn)):
                                if(len(remainingBoards) == 1):
                                    finalBall = True
                                    winningBall = ball
                                else:
                                    remainingBoards.remove(board)
                                break

    def solution(self) -> None:
        print("")
        day = "**** Day 4: Giant Squid ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
