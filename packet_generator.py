import numpy as np


# Packet generator class for different distributions
# Primary function is to return the next event_time
class PacketGenerator:
    def __init__(self, distribution, settings):
        self.distribution = distribution
        self.settings = settings

        self.mapping = {
            'poisson': self.poisson(),
            'deterministic': self.deterministic()
        }

    def number_of_packets(self):
        return self.mapping.get(self.distribution)

    # Poisson process
    def poisson(self):
        return np.random.poisson(self.settings.get('mean'))

    # Deterministic process
    def deterministic(self):
        return self.settings.get('mean')
