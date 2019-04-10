class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            print(left, right)
            m = (left + right) // 2
            if nums[m] < m + 1:
                right = m
            else:
                left = m

        return nums[left]

s = Solution()

print(s.findDuplicate([1,2,3,4,4,5]))