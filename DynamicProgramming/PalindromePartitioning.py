"""
LintCode 108: parlindrome partitioning

https://www.lintcode.com/problem/palindrome-partitioning-ii/description?_from=ladder&&fromId=16
"""


class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        # write your code here
        n = len(s)
        # Initialize the array
        # value: minCut till its index
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        is_pal = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if s[i - 1] == s[j] and (i - j <= 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1] - 1