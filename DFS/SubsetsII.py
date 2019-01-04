class Solution1(object):
    def subsetsWithDup(self, nums):
        self.ans = []
        nums.sort()
        self.dfs(nums, [])
        return self.ans

    def dfs(self, nums, path):
        self.ans.append(path)
        for i, n in enumerate(nums):
            # avoid duplicates
            if i > 0 and n == nums[i - 1]:
                continue
            self.dfs(nums[i + 1:], path + [n])

# Q: HOW TO REMOVE THE DUPLICATES?
# To avoid duplicates, for example: [1, 2, 2, 2, 3]
# If the current path is [1], which means for loop starts from index 1 (the first 2)
# Then we only go dfs for the first 2, skip dfs for the second and the third 2.

# When we're at [1, 2], which means the for loop starts from index 2 (the second 2)
# Then we only go dfs for the second 2, skip dfs for the third 3.

s = Solution1()
nums = [1, 1]
print('answer is', s.subsetsWithDup(nums))