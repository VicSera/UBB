class Directions:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    ALL = (UP, DOWN, LEFT, RIGHT)

class Cells:
    WALL = 1
    EMPTY = 0
    SENSOR = 2
    MARKED = 3