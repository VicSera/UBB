from queue import PriorityQueue

from taks1.domain.constants import UP, DOWN, LEFT, RIGHT, v


class SearchService:
    def __init__(self):
        pass

    def searchAStar(self, mapM, droneD, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        def distance(currentX, currentY, targetX, targetY):
            # compute the taxicab distance between the two points
            return abs(currentX - targetX) + abs(currentY - targetY)

        def isValidMove(x, y, path):
            return x in range(20) and y in range(20) \
                   and mapM.surface[x][y] == 0 \
                   and (x, y) not in path

        def reconstructPath(initialX, initialY, finalX, finalY, parent):
            path = []
            currentX, currentY = finalX, finalY
            path.append((currentX, currentY))
            while currentX != initialX or currentY != initialY:
                currentX, currentY = parent[(currentX, currentY)]
                path.append((currentX, currentY))
            path.reverse()
            return path

        path = [(initialX, initialY)]
        queue = PriorityQueue()
        parent = {}
        steps = {}

        queue.put((distance(initialX, initialY, finalX, finalY), (initialX, initialY)))
        steps[(initialX, initialY)] = 0

        while not queue.empty():
            node = queue.get()
            currentX, currentY = node[1][0], node[1][1]
            if currentX == finalX and currentY == finalY:
                return reconstructPath(initialX, initialY, finalX, finalY, parent)
            for direction in UP, DOWN, LEFT, RIGHT:
                nextX, nextY = currentX + v[direction][0], currentY + v[direction][1]
                if isValidMove(nextX, nextY, path) and \
                        ((nextX, nextY) not in steps or steps[(currentX, currentY)] + 1 < steps[(nextX, nextY)]):
                    dist = distance(nextX, nextY, finalX, finalY)
                    steps[(nextX, nextY)] = steps[(currentX, currentY)] + 1
                    queue.put((dist, (nextX, nextY)))
                    parent[(nextX, nextY)] = currentX, currentY

        # If we got here, there isn't any path leading to our destination
        return None

    def searchGreedy(self, mapM, droneD, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        def distance(currentX, currentY, targetX, targetY):
            # compute the taxicab distance between the two points
            return abs(currentX - targetX) + abs(currentY - targetY)

        def isValidGreedyMove(x, y, dist, minDistance, path):
            return x in range(20) and y in range(20) \
                   and mapM.surface[x][y] == 0 \
                   and (x, y) not in path \
                   and (minDistance is None or dist < minDistance)

        path = [(initialX, initialY)]

        currentX = initialX
        currentY = initialY

        while currentX != finalX or currentY != finalY:
            minDistance = None
            bestX, bestY = None, None
            for direction in UP, DOWN, LEFT, RIGHT:
                nextX, nextY = currentX + v[direction][0], currentY + v[direction][1]
                dist = distance(nextX, nextY, finalX, finalY)
                if isValidGreedyMove(nextX, nextY, dist, minDistance, path):
                    bestX, bestY = nextX, nextY
                    minDistance = dist
            if minDistance is None:
                return path
            path.append((bestX, bestY))
            currentX, currentY = bestX, bestY

        return path
