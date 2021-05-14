from util import distance


class Entry:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y
        self.cluster = None

    def closestCluster(self, clusters: list):
        minDist = 99999
        closestCluster = None
        for cluster in clusters:
            dist = distance(self.x, self.y, cluster.x, cluster.y)
            if dist < minDist:
                minDist = dist
                closestCluster = cluster
        return closestCluster
