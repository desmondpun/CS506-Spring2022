from scipy import spatial
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    nom = A.symmetric_difference(B)
    den = A.union(B)
    dist = (len(nom)/len(den))
    return dist

def cosine_sim(x, y):
    return 1-spatial.distance.cosine(x, y)
# Feel free to add more
