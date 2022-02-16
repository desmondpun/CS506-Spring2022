from collections import defaultdict
from math import inf
from dis import dis
from sklearn import datasetsfrom.sim import euclidean_dist
import random
import csv
import numpy as np


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    average = [sum(x)/len(x) for x in zip(*points)]
    return average


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    centers = []
    clusters = np.unique(assignments)
    for assign in clusters:
        data = []
        for i in range(len(dataset)):
            if assignments[i] == assign :
                data.append(dataset[i])
        centroid = point_avg(data)
        centers.append(centroid)
    return np.array(centers)

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return euclidean_dist(a,b)

def distance_squared(a, b):
    return (distance(a,b)**2) 

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return np.random.choice(dataset, k)

def cost_function(clustering):
    assignment = list(clustering)
    cost = 0
    for i in range(len(assignment)):
        cluster = assignment[i]
        cost += point_avg(cluster)
    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    kpp = []
    for i in range(len(dataset)):
        point = dataset[i]
        cent_pt = 0
        for j in range(len(dataset)):
            dist = point - dataset[j]
            cent_pt += np.linalg.norm(dist)
        kpp.append(dist)
    kpp = (pp - np.min(kpp)) / (np.min(kpp) - np.max(kpp))

    k_cent = []
    for i inrange(k):
        idx = np.argmax(kpp)
        k_cent.append(dataset[idx])
        kpp[idx] = np.min(kpp)
    return k_cent


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
