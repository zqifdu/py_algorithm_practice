# #  ================================================
# #  ============ Magic strings  ===================
# #  ================================================
# Description
#
# Given the following rules:
# "a" must only be followed by "e".
# "e" must only be followed by "a" or "i".
# "i" must only be followed by "a", "e", "i"
#
# return the number of strings of length n that can created with the rules above


def magicStrings(n):
    dp = [[0] * 3 for _ in range(2)]
    dp[0] = [1, 1, 1]

    for i in range(1, n):
        # Number of strings ending with a of length i + 1
        dp[i % 2][0] = dp[(i - 1) % 2][1] + dp[(i - 1) % 2][2]
        dp[i % 2][1] = dp[(i - 1) % 2][0] + dp[(i - 1) % 2][2]
        dp[i % 2][2] = dp[(i - 1) % 2][1] + dp[(i - 1) % 2][2]

    return sum(dp[i % 2]) if n > 1 else sum(dp[0])


print(magicStrings(1))
print(magicStrings(2))
print(magicStrings(3))
print(magicStrings(4))
print(magicStrings(5))
print(magicStrings(6))
print(magicStrings(7))
print(magicStrings(8))
print(magicStrings(20))