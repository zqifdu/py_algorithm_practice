"""
LintCode 118
https://www.lintcode.com/problem/distinct-subsequences/description?_from=ladder&&fromId=16
"""
class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        m = len(S)
        n = len(T)
        if n == 0:
            return 1

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(i, m):
                if i == 0 and j == 0:
                    # if S[0] == T[0],  [T[0]] is a subsequence of [S[0]]
                    dp[i][j] = int(S[0] == T[0])
                elif i == 0:
                    # If S[j] == T[0], this equation contributes one subsequence, but T[0]
                    # might be a subsequence of S[:k] where k < j
                    dp[i][j] = dp[i][j - 1] + int(S[j] == T[i])
                else:
                    # When S[j] == T[i], then any subsequence pair of T[:i] and S[:j] appended by
                    # S[j] or T[i] is also a subsequence pair
                    if S[j] == T[i]:
                        dp[i][j] += dp[i - 1][j - 1]
                    # If S[j] != T[i], we only count the number of unique subsequence
                    # of S[:j] which equals T[:i+1]
                    dp[i][j] += dp[i][j - 1]

        return dp[n - 1][m - 1]