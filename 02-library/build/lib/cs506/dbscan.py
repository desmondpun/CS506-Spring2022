from .sim import euclidean_dist

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon


    def epsilon_neighborhood(P):
        #Add code here
        neighborhood = []
        for PN in range(len(self.dataset)):
            if euclidean_dist(self.dataset[PN], self.dataset[P]) <= self.epsilon:
                neighborhood.append(PN)
        return neighborhood

    def explore_and_assign_eps_neighborhood(P, cluster, assignments):
        #Add code here
        neighborhood = self.epsilon_neighborhood(P)
        while neighborhood:
            neighbor_of_P = neighborhood.pop()
            if assignments[neighbor_of_P] != 0:
                continue
            assignment[neighbor_of_P] = cluster

            next_neighborhood = self.epsilon_neighborhood(neighbor_of_P)
            if len(next_neighborhood) >= self.min_pts:
                # this is a cor point
                # its neighbors should be explored / assigned also
                neighborhood.extend(next_neighborhood)
        return assignments

    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        #Add code to function
        assignments = [0 for _ in range(len(self.dataset))]

        cluster = 1

        for P in range(len(self.dataset)):
            if assignments[P] != 0:
                #already part of a cluster
                continue
            if len(self.epsilon_neighborhood(P)) >= self.min_pts:
                #core point
                assignments = self.explore_and_assign_eps_neighborhodd(P, cluster, assignments)
            # else:
            #     #border or noise
            
            cluster += 1
        return assignments
