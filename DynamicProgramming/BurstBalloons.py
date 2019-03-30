"""
LintCode 168

https://www.lintcode.com/problem/burst-balloons/description?_from=ladder&&fromId=16

"""


def maxCoins(self, nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            for k in range(i, j + 1):
                left = nums[i - 1] if i > 0 else 1
                right = nums[j + 1] if j < n - 1 else 1
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + left * nums[k] * right)

    return dp[0][n - 1]