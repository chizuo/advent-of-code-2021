from classes.assets.day5.point import Point


class Straight:
    def __init__(self, firstPoint, secondPoint) -> None:
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.line = self.buildline()

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


class Diagonal:
    def __init__(self, firstPoint, secondPoint) -> None:
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.line = self.buildline()

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
        simple = False

        if(x1 == y1 and x2 == y2):
            simple = True

            if (x1 > x2):
                start = x2
                end = x1
            else:
                start = x1
                end = x2
        else:
            start = 0
            end = abs(x1-x2)
            x = x1
            y = y1

        while(start <= end):
            if(simple == True):
                line.append(Point(start, start))
                start += 1
            else:
                line.append(Point(x, y))
                start += 1
                if(x1 > x2 and y1 > y2):
                    x -= 1
                    y -= 1
                elif(x1 > x2 and y1 < y2):
                    x -= 1
                    y += 1
                elif(x1 < x2 and y1 > y2):
                    x += 1
                    y -= 1
                else:
                    x += 1
                    y += 1

        return line
