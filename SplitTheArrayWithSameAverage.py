# LeetCode 805

class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        ave = sum(A) / len(A)
        A.sort()

        i = bisect.bisect_left(A, ave)
        if A[i] == ave:
            return True