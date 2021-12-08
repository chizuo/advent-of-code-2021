class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        rep = 'Point(x:' + str(self.x) + ', y:' + str(self.y) + ')'
        return rep
