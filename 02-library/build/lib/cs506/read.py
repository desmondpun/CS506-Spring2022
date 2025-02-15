import csv
import numpy as np
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(csv_file_path)
    numpy_array = np.loadtxt(file, delimiter=",", order = 'C')
    print(numpy_array)
    return numpy_array

