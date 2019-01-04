class Solution:
    def maximumSubarray(self, nums):
        for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)


"""
解释：
这个动态规划的方法首先将问题划分成一些互斥的所有可能的解，即最大的子序列可能以任何元素结尾。这个时候用 dp[i]表示以第 i 个元素
结尾的子序列的最大可能和。
递推公式：dp[i+1] = max(dp[i] + nums[i+1], dp[i+1])
"""

