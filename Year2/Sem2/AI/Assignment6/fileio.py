from entry import Entry


def readData(fileName):
    entries = []
    with open(fileName) as file:
        next(file)
        for line in file:
            data = line.split(',')
            entries.append(Entry(data[0], float(data[1]), float(data[2])))
    return entries
