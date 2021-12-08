'''
We have considered BFS and DFS graph traversal algorithms in the previous lectures.
You task is to design an algorithms with breadth-first search that is able to find
the shortest path from a given source to a given destination. The maze is represented
by a two-dimensional list.

The (0,0) is the source and (4,4) is the destination. 0 represents walls or obstacles
and 1 is the valid cells we can include in the solution.
'''

import collections


class MazeSolver():

    def __init__(self, matrix):
        self.matrix = matrix
        # read as (1,0), (0,-1), (0,1), (-1,0)
        # There is probably a better implementation for this
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        # False, but needs to be false for all rows and columns
        # Maybe not, this is list comprehension
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):
        '''
        Check for cell validity
            Check if in bounds
            Check if cell is occupied or not
            Check if cell has been visited
        '''

        if row < 0 or row >= len(self.matrix):
            return False

        if col < 0 or col >= len(self.matrix):
            return False

        if not self.matrix[row][col]:
            return False

        if self.visited[row][col]:
            return False

        return True

    def solve(self, start_i, start_j, dest_i, dest_j):
        self.visited[start_i][start_j] = True
        queue = collections.deque()
        queue.append((start_i, start_i, 0))

        while queue:
            (i, j, dist) = queue.popleft()
            print(i, j)

            if i == dest_i and j == dest_j:
                self.min_distance = dist
                break

            # Test each move sequence
            for move in range(len(self.move_x)):
                print(move)
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                # if move sequence is valid, visit and enqueue
                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float("inf"):
            print("shortest path : ", self.min_distance)


if __name__ == "__main__":

    maze = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]]

    maze_solver = MazeSolver(maze)
    maze_solver.solve(0, 0, 4, 4)
    maze_solver.show_result()
