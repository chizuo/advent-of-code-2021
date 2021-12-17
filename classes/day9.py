from os import XATTR_SIZE_MAX


class SmokeBasin:
    def __init__(self) -> None:
        filepath = "./classes/assets/day9/input.txt"
        self.rowMax = 0
        self.colMax = 0
        self.input = self.scanFile(filepath)
        self.xLow = []
        self.yLow = []
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile(self, loc) -> list:
        with open(loc, 'r') as file:
            lines = file.readlines()
            grid = []
            for line in lines:
                row = []

                for char in line:
                    if(char.isnumeric()):
                        row.append(int(char))

                grid.append(row)
            self.colMax = len(grid[0])
            self.rowMax = len(grid)
            return grid

    def checkDirection(self, x, y) -> dict:
        check = {
            'Right': True,
            'Left': True,
            'Up': True,
            'Down': True
        }
        xMax = self.colMax
        yMax = self.rowMax

        if(x == xMax - 1):
            check["Right"] = False
        if(x == 0):
            check["Left"] = False
        if(y == 0):
            check["Up"] = False
        if(y == yMax - 1):
            check["Down"] = False

        return check

    def visit(self, point, x, y, visited, grid) -> bool:
        lowest = True
        check = self.checkDirection(x, y)

        if(check["Right"]):
            if(point < grid[y][x+1]):
                visited[y][x+1] = True
            else:
                lowest = False

        if(check["Left"]):
            if(point < grid[y][x-1]):
                visited[y][x-1] = True
            else:
                lowest = False

        if(check["Up"]):
            if(point < grid[y-1][x]):
                visited[y-1][x] = True
            else:
                lowest = False

        if(check["Down"]):
            if(point < grid[y+1][x]):
                visited[y+1][x] = True
            else:
                lowest = False

        return lowest

    def bfs(self, x, y) -> int:
        visited = [[False]*self.colMax for i in range(self.rowMax)]
        size = 0
        grid = self.input
        xQueue = [x]
        yQueue = [y]

        while(len(xQueue) > 0):
            x = xQueue.pop(0)
            y = yQueue.pop(0)
            if(not visited[y][x]):
                visited[y][x] = True
                size += 1
                check = self.checkDirection(x, y)

                if(check["Right"]):
                    if(9 > grid[y][x+1]):
                        if(not visited[y][x+1]):
                            yQueue.append(y)
                            xQueue.append(x+1)
                if(check["Left"]):
                    if(9 > grid[y][x-1]):
                        if(not visited[y][x-1]):
                            yQueue.append(y)
                            xQueue.append(x-1)
                if(check["Up"]):
                    if(9 > grid[y-1][x]):
                        if(not visited[y-1][x]):
                            yQueue.append(y-1)
                            xQueue.append(x)
                if(check["Down"]):
                    if(9 > grid[y+1][x]):
                        if(not visited[y+1][x]):
                            yQueue.append(y+1)
                            xQueue.append(x)

        return size

    def part1(self) -> int:
        visited = [[False]*self.colMax for i in range(self.rowMax)]
        points = []

        for y in range(self.rowMax):
            for x in range(self.colMax):
                if(visited[y][x] == True):
                    continue
                else:
                    point = self.input[y][x]
                    visited[y][x] = True
                    if(self.visit(point, x, y, visited, self.input)):
                        points.append(point)
                        self.xLow.append(x)
                        self.yLow.append(y)

        return sum(points) + len(points)

    def part2(self) -> int:
        basin = []
        product = 1

        for i in range(len(self.xLow)):
            basin.append(self.bfs(self.xLow[i], self.yLow[i]))

        basin.sort(reverse=True)

        return basin[0]*basin[1]*basin[2]

    def solution(self) -> None:
        print("")
        day = "**** Day 9: Smoke Basin ****"
        print(day)
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
        for char in day:
            print("*", end="")
