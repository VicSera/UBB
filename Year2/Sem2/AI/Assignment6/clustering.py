import random

from entry import Entry

RANGE = 10
N_CLUSTERS = 4


class Cluster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.entries: list[Entry] = []

    def recomputeCentroid(self):
        # return True if the centroid changed, False otherwise
        if len(self.entries) == 0:
            return False

        x = [entry.x for entry in self.entries]
        y = [entry.y for entry in self.entries]

        newX = sum(x) / len(self.entries)
        newY = sum(y) / len(self.entries)

        changed = False
        if newX != self.x or newY != self.y:
            changed = True

        self.x = newX
        self.y = newY

        return changed


def randomClusters(k: int):
    clusters = []
    for _ in range(k):
        clusters.append(Cluster(random.random() * RANGE, random.random() * RANGE))
    return clusters


def reassignEntries(entries: list[Entry], clusters: list[Cluster]):
    for entry in entries:
        # Compute the closest cluster
        closestCluster = entry.closestCluster(clusters)

        # Remove the entry from its old cluster
        if entry.cluster is not None:
            entry.cluster.entries.remove(entry)

        # Assign the cluster in the entry
        entry.cluster = closestCluster

        # Add the entry in the cluster
        closestCluster.entries.append(entry)


def recomputeCentroids(clusters: list[Cluster]):
    # Recompute the centroid of each cluster
    # Returns True if at least one centroid changed, False if none changed
    changed = False
    for cluster in clusters:
        changed = changed or cluster.recomputeCentroid()
    return changed
