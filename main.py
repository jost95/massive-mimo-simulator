import json
import time

from stats import Stats
from logger import Logger
from simulation import Simulation

if __name__ == '__main__':
    # Set a custom simulation name, stats for simulations with the same name will be saved to the same file
    simulation_name = 'original'
    time_string = time.strftime('%Y%m%d_%H%M%S')

    # Load simulation parameters
    with open('config.json') as f:
        config = json.load(f)

    # Initialize a new logger
    log_file_path = 'logs/' + time_string + simulation_name + '_queue_log.csv'
    logger = Logger(log_file_path)

    # Initialize a new statistics object
    stats_file_path = 'stats/' + simulation_name + '_stats.csv'
    stats = Stats(stats_file_path)

    # Run the simulation
    simulation = Simulation(config, logger, stats)
    simulation.run()

    # Close files and save results
    logger.close()
    stats.print()
    stats.save_and_close()
