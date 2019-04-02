"""
https://www.lintcode.com/problem/maximum-gap/description?_from=ladder&&fromId=4
"""


class Solution:
    # @param nums: a list of integers
    # @return: the maximum difference
    def maximumGap(self, nums):
        if (len(nums) < 2):
            return 0

        # Find the max number the and minimum number
        minNum = 0x7fffffff
        maxNum = -0x7fffffff

        n = len(nums)

        for i in range(n):
            minNum = min(nums[i], minNum)
            maxNum = max(nums[i], maxNum)

        if maxNum == minNum:
            return 0

        # average distance between neighboring elements
        average = (maxNum - minNum) * 1.0 / (n - 1)

        if average < 1:
            average += 1
        average = int(average)

        localMin = [0x7fffffff + 1] * n
        localMax = [-0x7fffffff - 1] * n

        for i in range(n):
            t = int((nums[i] - minNum) / average)
            localMin[t] = min(localMin[t], nums[i])
            localMax[t] = max(localMax[t], nums[i])

        ans = average
        left = 0
        right = 1
        while left < n - 1:
            while right < n and localMin[right] == 0x7fffffff + 1:
                right += 1
            if right >= n:
                break
            ans = max(ans, localMin[right] - localMax[left])
            left = right
            right += 1
        return ans
