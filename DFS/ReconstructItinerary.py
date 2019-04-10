"""
https://leetcode.com/problems/reconstruct-itinerary/

"""
import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)

        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]


if __name__ == '__main__':
    s = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(s.findItinerary(tickets))