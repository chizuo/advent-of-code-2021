from classes.assets.day5.point import Point
from classes.assets.day5.line import Straight
from classes.assets.day5.line import Diagonal
import copy


class HydrothermalVenture:
    def __init__(self) -> None:
        filepath = "./classes/assets/day5/input.txt"
        self.straightClouds = []
        self.diagonalClouds = []
        self.xmax = 0
        self.ymax = 0
        self.scanFile(filepath)
        self.grid = self.buildGrid()
        self.part1solution = self.part1()
        self.part2solution = self.part2()

    def scanFile(self, loc) -> list:
        with open(loc, "r") as file:
            count = 1
            straight = []
            diagonal = []
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

                # Vertical or Horizontal Straight Line
                if(points[0].x == points[1].x or points[0].y == points[1].y):
                    straight.append(Straight(points[0], points[1]))

                # Diagonal Line
                if(points[0].x == points[0].y and points[1].x == points[1].y):
                    diagonal.append(Diagonal(points[0], points[1]))
                else:
                    difference = abs(
                        points[0].x - points[1].x) - abs(points[0].y - points[1].y)
                    if(difference == 0):
                        diagonal.append(Diagonal(points[0], points[1]))

            self.xmax = xmax+1
            self.ymax = ymax+1
            self.straightClouds = straight
            self.diagonalClouds = diagonal

    def buildGrid(self) -> None:
        grid = []

        for row in range(self.ymax):
            grid.append([0]*self.xmax)

        return grid

    def part1(self) -> None:
        # list of objects (Line), representing an opaque cloud. The lines are a list of objects (Point) that contain x and y coordinates (int)
        clouds = self.straightClouds
        grid = copy.deepcopy(self.grid)
        intersect = 0

        for cloud in clouds:
            for point in cloud.line:
                value = grid[point.y][point.x]
                value += 1
                grid[point.y][point.x] = value

        for row in grid:
            for element in row:
                if(element > 1):
                    intersect += 1

        return intersect

    def part2(self) -> None:
        clouds = self.straightClouds + self.diagonalClouds
        grid = copy.deepcopy(self.grid)
        intersect = 0

        for cloud in clouds:
            for point in cloud.line:
                value = grid[point.y][point.x]
                value += 1
                grid[point.y][point.x] = value

        for row in grid:
            for element in row:
                if(element > 1):
                    intersect += 1

        return intersect

    def solution(self) -> None:
        print("\n**** Day 5: Hydrothermal Venture ****")
        print("Part 1: ", self.part1solution)
        print("Part 2: ", self.part2solution)
