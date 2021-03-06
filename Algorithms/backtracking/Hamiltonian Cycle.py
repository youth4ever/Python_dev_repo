#  Created by Bogdan Trif on 26-10-2017 , 11:24 AM.
'''

https://en.wikipedia.org/wiki/Hamiltonian_path
Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once.
A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in graph)
from the last vertex to the first vertex of the Hamiltonian Path.
Determine whether a given graph contains Hamiltonian Cycle or not.
If it contains, then print the path. Following are the input and output of the required function.

Input:
A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency matrix
representation of the graph. A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.

Output:
An array path[V] that should contain the Hamiltonian Path.
path[i] should represent the ith vertex in the Hamiltonian Path.
The code should also return false if there is no Hamiltonian Cycle in the graph.

For example, a Hamiltonian Cycle in the following graph is {0, 1, 2, 4, 3, 0}.
There are more Hamiltonian Cycles in the graph like {0, 3, 4, 2, 1, 0}

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)-------(4)
And the following graph doesn’t contain any Hamiltonian Cycle.

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)      (4)

'''

# Python program for solution of
# hamiltonian cycle problem

class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]\
                            for row in range(vertices)]
        self.V = vertices

    ''' Check if this vertex is an adjacent vertex 
        of the previously added vertex and is not 
        included in the path earlier '''
    def isSafe(self, v, pos, path):
        # Check if current vertex and last vertex
        # in path are adjacent
        if self.graph[ path[pos-1] ][v] == 0:
            return False

        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    # A recursive utility function to solve
    # hamiltonian cycle problem
    def hamCycleUtil(self, path, pos):

        # base case: if all vertices are
        # included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cyle
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in in hamCycle()
        for v in range(1,self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos+1) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        ''' Let us put vertex 0 as the first vertex 
            in the path. If there is a Hamiltonian Cycle, 
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path,1) == False:
            print ("Solution does not exist\n")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print( "Solution Exists: Following is one Hamiltonian Cycle")
        for vertex in path:
            print( vertex,)
        print (path[0], "\n")

# Driver Code

''' Let us create the following graph
      (0)--(1)--(2)
       |   / \   |
       |  /   \  |
       | /     \ |
      (3)-------(4)    '''
g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0], ]

# Print the solution
g1.hamCycle();

''' Let us create the following graph
      (0)--(1)--(2)
       |   / \   |
       |  /   \  |
       | /     \ |
      (3)       (4)    '''
g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
           [0, 1, 1, 0, 0], ]

# Print the solution
g2.hamCycle();

# This code is contributed by Divyanshu Mehta

