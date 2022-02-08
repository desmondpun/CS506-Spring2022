import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data