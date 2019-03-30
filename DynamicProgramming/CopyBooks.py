"""
LintCode 437
https://www.lintcode.com/problem/copy-books/description?_from=ladder&&fromId=16

"""


# Solution 1: binary search
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0

        min_time, max_time = max(pages), sum(pages)

        while min_time + 1 < max_time:
            mid = (min_time + max_time) // 2

            if self.can_finish(pages, k, mid):
                max_time = mid

            else:
                min_time = mid

        if self.can_finish(pages, k, min_time):
            return min_time
        return max_time

    def can_finish(self, pages, k, time):
        curr = 0
        for page in pages:
            curr += page
            if curr > time:
                k -= 1
                curr = page
        return k - 1 >= 0


# Solution 2: Dynamic programming

# class Solution2:
#     def copyBooks(self, pages, k):
