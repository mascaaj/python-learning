"""
Travelling salesman problem implementation
Uses adjacency matrix representation for graph
22FEB22
"""


class TravellingSalesman:

    def __init__(self, graph):
        # Matrix representation
        self.graph = graph
        # symmetric, number of vertices
        self.n = len(graph)
        # initialize as false, start at 1st vertex
        # could be random
        self.visited = [False for _ in range(self.n)]
        self.visited[0] = True
        # structure to store all cycles, need min cycle
        self.hamiltonian_cycle = []
        # tracking vertices in the cycle
        self.path = [0 for _ in range(self.n)]

    def is_valid(self, vertex, actual_position):
        # actual_position is current location
        # vertex is every other position to be considered
        """
        Check if vertex has been visited
        Check if vertex has connection
        (has connection in graph = checking position in matrix not zero)
        """
        if self.visited[vertex]:
            return False

        if self.graph[vertex][actual_position] == 0:
            return False

        return True

    def tsp(self, actual_position, counter, cost):
        """
        Base case
            if all the vertices are visited
            if actual position is connected to starting vertex
        Consider all vertices
        if valid, increment counter, visited
        recursively call function

        If base condition is met, hcycle is added to list
        If not met, backtracking comes into play when stack frame is removed
        """
        if counter == self.n and self.graph[actual_position][0]:
            self.path.append(0)
            print(self.path)
            self.hamiltonian_cycle.append(cost + self.graph[actual_position][0])
            self.path.pop()
            return

        for i in range(self.n):
            if self.is_valid(i, actual_position):
                self.path[counter] = i
                self.visited[i] = True

                # call function recursively
                self.tsp(i, counter + 1, cost + self.graph[actual_position][i])

                # BACKTRACKING - when the recursive function returns
                # it will mark the just visited node false
                # but will increment in outer for loop
                self.visited[i] = False


if __name__ == "__main__":

    g = [[0, 1, 0, 2, 0],
         [1, 0, 1, 0, 2],
         [0, 1, 0, 3, 1],
         [2, 0, 3, 0, 1],
         [0, 2, 1, 1, 0]]

    tsp = TravellingSalesman(g)
    tsp.tsp(0, 1, 0)
    print(tsp.hamiltonian_cycle)
