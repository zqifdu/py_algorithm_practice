# https://leetcode.com/problems/valid-permutations-for-di-sequence/description/

class Solution:

    # DFS: time limit excess
    def numPermsDISequence1(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [[i] for i in range(len(S) + 1)]
        ans = 0

        nums = set(range(len(S) + 1))

        while stack:
            ls = stack.pop()
            if len(ls) == len(nums):
                ans += 1
                continue
            l_ls = len(ls)
            left = nums - set(ls)
            trend = S[l_ls - 1]
            for l in left:
                if trend == 'D' and l < ls[-1]:
                    stack.append(ls + [l])
                if trend == 'I' and l > ls[-1]:
                    stack.append(ls + [l])
        return ans

    # Dynamic programming
    def numPermsDISequence(self, S):
        # todo
        pass
