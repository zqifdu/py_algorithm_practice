"""
LintCode 92
https://www.lintcode.com/problem/backpack/description?_from=ladder&&fromId=16
"""

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        n = len(A)
        # Index:    total weights
        # Value:    the last item in the bag in A to get this total wegihts
        dp = [n + 1] * (m + 1)
        dp[0] = -1

        max_weight = 0
        for i in range(1, m + 1):
            for j, w in enumerate(A):
                if i - w >= 0 and dp[i - w] != n + 1 and j > dp[i - w]:
                    dp[i] = min(dp[i], j)
                    max_weight = i

        return max_weight



    # Solution 2: https://www.jiuzhang.com/solution/backpack/#tag-highlight-lang-python
    '''
    效率最高的算法，没有之一。算法为区间合并。

    比如，输入的整数是 [1,2,5]。当一个物品都不选的时候，可以组成的最大和为 0，也就是 [0,0] 这段区间可以被组成。

    当有 1 以后，把 [0,0] 的左右两边都+1，得到 [1,1]，然后合并 [0,0] 和 [1,1] 得到 [0,1]
    加入2以后，意味着，原本可以从前面的数里组成 [0,1] 区间中的任何和，现在可以组成 [0,1]里面的任意和加上 [0+2,1+2] 里的任意和。
    也就是 [0,1] + [2,3]，合并之后等于 [0,3]
    最后加入5。 [0,3] + [5,8] => [[0,3],[5,8]]
    
    这样就得到了这些物品能够组成的和有哪些（以区间的形式存储）。然后看看 <= m 里最大被覆盖到的数是谁即可。
    '''
    def backPack_2(self, m, A):
        A.sort()

        intervals = [[0, 0]]
        for item in A:
            new_intervals = []
            for interval in intervals:
                new_intervals.append([interval[0] + item, interval[1] + item])

            intervals = self.merge_intervals(intervals, new_intervals)

        max_size = 0
        for interval in intervals:
            if interval[0] <= m <= interval[1]:
                return m
            if interval[0] > m:
                break
            max_size = max(max_size, interval[1])
        return max_size

    def merge_intervals(self, list1, list2):
        i, j = 0, 0
        intervals = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                self.push_to_intervals(intervals, list1[i])
                i += 1
            else:
                self.push_to_intervals(intervals, list2[j])
                j += 1

        while i < len(list1):
            self.push_to_intervals(intervals, list1[i])
            i += 1

        while j < len(list2):
            self.push_to_intervals(intervals, list2[j])
            j += 1

        return intervals

    def push_to_intervals(self, intervals, interval):
        if not intervals or intervals[-1][1] + 1 < interval[0]:
            intervals.append(interval)
            return

        intervals[-1][1] = max(intervals[-1][1], interval[1])