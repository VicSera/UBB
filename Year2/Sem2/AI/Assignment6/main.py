from clustering import randomClusters, N_CLUSTERS, recomputeCentroids, reassignEntries
from fileio import readData
from stats import computeLabelsAndStats, displayCharts

if __name__ == '__main__':
    entries = readData('dataset.csv')
    clusters = randomClusters(N_CLUSTERS)

    centroidsChanged = True
    while centroidsChanged:
        reassignEntries(entries, clusters)
        centroidsChanged = recomputeCentroids(clusters)

    result = computeLabelsAndStats(entries, clusters)

    for key, value in result["Stats"].items():
        print(key + ": " + str(value))

    colors = {
        "A": "red",
        "B": "blue",
        "C": "green",
        "D": "yellow"
    }
    displayCharts(entries, result["Labels"], colors, clusters)