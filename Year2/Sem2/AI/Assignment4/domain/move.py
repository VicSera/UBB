class Move:
    def __init__(self, sensor, energy):
        self.sensor = sensor
        self.energy = energy

    @property
    def score(self):
        return self.sensor.scoreAtEnergyLevel[self.energy]