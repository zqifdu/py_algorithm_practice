"""
https://leetcode.com/problems/redundant-connection-ii/discuss/182655/Union-Find-with-a-few-of-explanations-on-key-points...
"""


class unionFind():
    def __init__(self, length):
        self.parent = list(range(length + 1))
        self.rnk = [0] * (length + 1)

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.rnk[a] < self.rnk[b]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            if self.rnk[pa] == self.rnk[pb]:
                self.rnk[pa] += 1
        return True

    def find(self, a):
        while a != self.parent[a]:
            # path compression
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a


class Solution:
    def findRedundantDirectedConnection(self, edges):
        if not edges:
            return None
        c1 = (0, 0)
        c2 = (0, 0)

        parent = [0] * (len(edges) + 1)
        for edge in edges:
            if parent[edge[1]] != 0:
                c1 = (parent[edge[1]], edge[1])
                c2 = (edge[0], edge[1])
                break
            parent[edge[1]] = edge[0]

        uf = unionFind(len(edges))
        for edge in edges:
            if (edge[0] == c1[0] and edge[1] == c1[1]) or (edge[0] == c2[0] and edge[1] == c2[1]):
                continue
            if not uf.union(edge[0], edge[1]):
                return edge

        if not uf.union(c1[0], c1[1]):
            return c1
        return c2