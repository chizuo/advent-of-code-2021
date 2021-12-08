from classes.assets.day5.point import Point
from classes.assets.day5.line import Line
import copy


class HydrothermalVenture:
    def __init__(self) -> None:
        filepath = "./classes/assets/day5/input.txt"
        self.inputStraight = self.scanFileP1(filepath)
        self.inputDiagonal = self.scanFileP2(filepath)
        self.grid = self.buildGrid()
        self.xmax = 0
        self.ymax = 0
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFileP1(self, loc) -> list:
        with open(loc, "r") as file:
            count = 1
            clouds = []
            xmax = 0
            ymax = 0

            for line in file:
                number = ''
                points = []
                count = 1
                line = line.strip()
                lastchar = len(line)

                for char in line:
                    if(char.isdigit()):
                        number += char

                    if(char == ","):
                        x = int(number)
                        xmax = x if x > xmax else xmax
                        number = ''

                    if(char == '-' or count == lastchar):
                        y = int(number)
                        ymax = y if y > ymax else ymax
                        points.append(Point(x, y))
                        number = ''

                    count += 1

                if(points[0].x == points[1].x or points[0].y == points[1].y):
                    clouds.append(Line(points[0], points[1]))
            self.xmax = xmax+1
            self.ymax = ymax+1
            return clouds

    def scanFileP2(self, loc) -> list:
        pass

    def buildGrid(self) -> None:
        grid = []

        for row in range(self.ymax):
            grid.append([0]*self.xmax)

        return grid

    def part1(self) -> None:
        # list of objects (Line), representing an opaque cloud. The lines are a list of objects (Point) that contain x and y coordinates (int)
        clouds = self.inputStraight
        grid = copy.deepcopy(self.grid)
        intersect = 0

        for cloud in clouds:
            for point in cloud.straightline:
                value = grid[point.y][point.x]
                value += 1
                grid[point.y][point.x] = value

        for row in grid:
            for element in row:
                if(element > 1):
                    intersect += 1

        return intersect

    def part2(self) -> None:
        return "In Progress"

    def solution(self) -> None:
        print("\n**** Day 5: Hydrothermal Venture ****")
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
