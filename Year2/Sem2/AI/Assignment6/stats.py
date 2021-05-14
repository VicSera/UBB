from collections import OrderedDict
from itertools import permutations
from matplotlib.pyplot import scatter, show, subplots

from entry import Entry
from clustering import Cluster


def computeStatistics(entries: list[Entry], clusterToLabel):
    TP = FP = TN = FN = 0
    TOTAL = len(entries)

    for entry in entries:
        if entry.label != clusterToLabel[entry.cluster]:
            FP += 1
            FN += 1
            TN += 2
        else:
            TP += 1
            TN += 3

    A = (TP + TN) / TOTAL
    P = TP / (TP + FP) if TP + FP != 0 else 0
    R = TP / (TP + FN) if TP + FN != 0 else 0
    S = 2 * P * R / (P + R) if P + R != 0 else 0
    return {
        "Accuracy": A,
        "Precision": P,
        "Rappel": R,
        "Score": S
    }


def computeLabelsAndStats(entries: list[Entry], clusters: list[Cluster]):
    bestLabels = None
    bestStats = {}
    for labelPermutation in list(permutations(['A', 'B', 'C', 'D'])):
        clusterToLabel = {clusters[i]: labelPermutation[i] for i in range(4)}
        stats = computeStatistics(entries, clusterToLabel)

        if "Score" not in bestStats.keys() or bestStats["Score"] < stats["Score"]:
            bestLabels = clusterToLabel
            bestStats = stats

    return {
        "Labels": bestLabels,
        "Stats": bestStats
    }


def displayCharts(entries: list[Entry], clusterToLabel: dict, labelToColor: dict, clusters: list[Cluster]):
    x = [entry.x for entry in entries]
    y = [entry.y for entry in entries]
    correctColors = [labelToColor[entry.label] for entry in entries]
    guessedColors = [labelToColor[clusterToLabel[entry.cluster]] for entry in entries]


    fig, (ax1, ax2) = subplots(1, 2)
    fig.suptitle("Actual clusters and obtained clusters")
    ax1.scatter(x, y, c=correctColors)
    ax2.scatter(x, y, c=guessedColors)
    ax1.axis('equal')
    ax2.axis('equal')
    for cluster in clusters:
        ax2.text(cluster.x, cluster.y, clusterToLabel[cluster])
    for label in labelToColor:
        x = [entry.x for entry in filter(lambda entry: entry.label == label, entries)]
        y = [entry.y for entry in filter(lambda entry: entry.label == label, entries)]
        avgX = sum(x) / len(x)
        avgY = sum(y) / len(y)
        ax1.text(avgX, avgY, label)
    show()

