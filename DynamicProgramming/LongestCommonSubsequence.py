class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        n = len(A)
        m = len(B)
        if n == 0 or m == 0:
            return 0
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = int(A[i] == B[j])
                elif i == 0:
                    dp[i][j] = max(dp[i][j - 1], int(A[i] == B[j]))
                elif j == 0:
                    dp[i][j] = max(dp[i - 1][j], int(A[i] == B[0]))
                else:
                    if A[i] == B[j]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i][j])
        return dp[n - 1][m - 1]