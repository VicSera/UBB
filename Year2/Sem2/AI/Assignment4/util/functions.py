from util.environmentUtils import Cells


def isValidPosition(position: tuple, env):
    return position[0] in range(env.size) and position[1] in range(env.size) and \
           env.cells[position[0]][position[1]] != Cells.WALL


def taxicabDistance(pos1: tuple, pos2: tuple):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def distance(currentX, currentY, targetX, targetY):
    # compute the taxicab distance between the two points
    return abs(currentX - targetX) + abs(currentY - targetY)
