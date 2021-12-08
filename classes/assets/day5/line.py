from classes.assets.day5.point import Point


class Line:
    def __init__(self, firstPoint, secondPoint) -> None:
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.straightline = self.buildline()
        self.line = self.buildDiagonalLines()

    def __repr__(self) -> str:
        rep = 'Line: '
        for entry in self.line:
            rep += str(entry) + ' '

        return rep

    def buildline(self) -> list:
        x1 = self.firstPoint.x
        y1 = self.firstPoint.y
        x2 = self.secondPoint.x
        y2 = self.secondPoint.y

        line = []
        x = False

        # logic that determines which coordinate is equal to build either a vertical or horizontal line
        if(x1 == x2):
            x = True
            if(y1 > y2):
                start = y2
                end = y1
            else:
                start = y1
                end = y2
        else:
            if(x1 > x2):
                start = x2
                end = x1
            else:
                start = x1
                end = x2

        # builds the line representing the opaque cloud as a list of points that form a straight line
        while(start <= end):
            if(x == True):
                line.append(Point(x1, start))
            else:
                line.append(Point(start, y1))
            start += 1

        return line

    def buildDiagonalLines(self) -> list:
        pass
