"""
LintCode 29 Interleaving String
https://www.lintcode.com/problem/interleaving-string/description?_from=ladder&&fromId=16

"""

def isInterleave(self, s1, s2, s3):
    # write your code here
    if len(s3) != len(s1) + len(s2):
        return False

    if not s3:
        return True

    if not s1:
        return s3 == s2

    if not s2:
        return s1 == s3

    m, n, l = len(s1), len(s2), len(s3)

    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            ch3 = s3[i + j - 1]
            if i == 0 and j == 0:
                dp[0][0] = True
                continue
            if ch3 == s1[j - 1]:
                dp[i][j] |= dp[i][j-1]
            if ch3 == s2[i - 1]:
                dp[i][j] |= dp[i-1][j]

    return dp[n][m]