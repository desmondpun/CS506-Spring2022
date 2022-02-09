import csv
import numpy as np
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(csv_file_path)
    numpy_array = np.loadtxt(file, delimiter=",")
    return [item for sublist in numpy_array for item in sublist]

