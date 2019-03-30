class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        # write your code here
        if m == 0:
            return 0

        if not A:
            return 0

        dp = [0] * (m + 1)

        dp[0] = 0

        for w in range(1, m + 1):
            for item in range(len(A)):
                if w - A[item] >= 0:
                    dp[w] = max(dp[w - A[item]] + V[item], dp[w])

        for i in range(w, -1, -1):
            if dp[i] != 0:
                return dp[i]
