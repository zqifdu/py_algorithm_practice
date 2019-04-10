"""
https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
"""

class Graph():
    def __init__(self, nVertices):
        self.graph = [[0 for column in range(nVertices)] for row in range(nVertices)]
        self.numV = nVertices


def hamCycle(graph):
    numV = graph.numV
    visited = 0
    path = []
    for i in range(numV):
        visited |= (1<<i)
        path.append(i)
        if dfs(graph, i, visited, path):
            return path[::-1]
        else:
            path = []
    return -1


def dfs(graph, start, visited, path):
    if visited == 2 ** (graph.numV) - 1 and path and graph.graph[start][path[0]] == 1:
        return True

    for i in range(graph.numV):
        if graph.graph[start][i] and not visited & (1 << i):
            path.append(i)
            visited |= (1 << i)
            if dfs(graph, i, visited, path):
                return True
            else:
                path.pop()

    return False


if __name__ == '__main__':
    g1 = Graph(5)
    g1.graph = [[0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0], ]
    print(hamCycle(g1))

