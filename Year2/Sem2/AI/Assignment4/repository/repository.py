import pickle


class Repository:
    def __init__(self):
        self.environment = None

    def saveObject(self, object, path):
        with open(path, mode = "wb") as file:
            pickle.dump(object, file)

    def loadObject(self, path):
        with open(path, mode = "rb") as file:
            return pickle.load(file)
