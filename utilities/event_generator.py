import numpy as np

__author__ = "Jon Stålhammar, Christian Lejdström, Emma Fitzgerald"


class EventGenerator:
    """
        Generates event times given a certain distribution

        Attributes
        ----------
        distribution : str
            A specified and valid distribution. Currently supports:
                - Exponential
                - Constant
        settings : dict
            Dictionary of parameters for the specified distribution. Needed parameters are:
                - Exponential: mean_arrival_time (mean arrival time)
                - Constant: arrival_time (arrival time)
        use_seed : bool
            Specifies if a seed should be used for the random number generation

    """

    def __init__(self, distribution, settings):
        """
        Initializes a new event generator. See class documentation for parameters explanation.

        Parameters
        ----------
        distribution : str
            See class documentation
        settings : dict
            See class documentation
        """

        self.__distribution = distribution
        self.__settings = settings

        self.mapping = {
            'exponential': self.__exponential,
            'uniform': self.__uniform,
            'constant': self.__constant
        }

    def get_next(self):
        """
        Generates a new event time given specified distribution

        Returns
        -------
        float
            A float with the next event time
        """

        return self.mapping[self.__distribution]()

    def __exponential(self):
        # Returns float from an exponential distribution

        return np.random.exponential(self.__settings.get('mean_arrival_time'))

    def __uniform(self):
        # Return float from a uniform distribution

        return np.random.uniform(0, self.__settings.get('max_arrival_time'))

    def __constant(self):
        # Returns a float from a constant distribution

        return self.__settings.get('arrival_time')
