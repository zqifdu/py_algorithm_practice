"""
https://leetcode.com/problems/redundant-connection/
"""


class UnionSet(object):
    def __init__(self):
        self.sets = dict()

    def find(self, target):
        for key in self.sets.keys():
            if target == key:
                return key
            if target in self.sets[key]:
                return key
        return None

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        # print(node1, node2, parent1, parent2)
        if (not parent1) and (parent2 is not None):
            self.sets[parent2] += [node1]
        elif (not parent2) and (parent1 is not None):
            self.sets[parent1] += [node2]
        elif not (parent1 or parent2):
            self.sets[node1] = [node2]
        else:
            if parent1 == parent2:
                return False
            else:
                large_parent = parent1 if len(self.sets[parent1]) > len(self.sets[parent2]) else parent2
                small_parent = parent1 if large_parent == parent2 else parent2
                self.sets[large_parent] += (self.sets[small_parent] + [small_parent])
                del self.sets[small_parent]
                return True


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        sets = UnionSet()
        for edge in edges:
            union_succeed = sets.union(*edge)
            if union_succeed is False:
                return edge


# Online Solution
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge