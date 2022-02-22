"""
Dijkstra algorithm with matrix representation
18FEB22
"""
import sys


class Dijkstra:

    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        self.distances = [float("inf") for _ in range(len(adjacency_matrix))]
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0

    def get_min_vertex(self):
        min_vertex_value = sys.maxsize
        min_vertex_index = 0

        for index in range(self.v):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index
        return min_vertex_index

    def calculate(self):
        for index in range(self.v):
            actual_vertex = self.get_min_vertex()
            print("considering vertex : ", actual_vertex)
            self.visited[actual_vertex] = True

            for other_vertex in range(self.v):
                # check if there is a connection
                if self.adjacency_matrix[actual_vertex][other_vertex] > 0:
                    if (self.distances[actual_vertex] +
                       self.adjacency_matrix[actual_vertex][other_vertex] <
                       self.distances[other_vertex]):

                        self.distances[other_vertex] = (self.distances[actual_vertex] +
                                                        self.adjacency_matrix[actual_vertex][other_vertex])

    def print_distances(self):
        print("distances : ", self.distances)


if __name__ == "__main__":

    # Define the nodes
    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]
    algorithm = Dijkstra(m, 1)
    algorithm.calculate()
    algorithm.print_distances()
