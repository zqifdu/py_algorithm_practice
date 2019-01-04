from collections import deque


class Solution3:
    """
    Dynamic programming
    Inverse array
    """
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        print('In function')
        A2 = A + A

        table = [0] * len(A2)

        if len(A) == 1:
            return A[0]

        ans = float('-inf')
        total = 0
        for i in range(len(A2)):
            total += A2[i]
            table[i] = total
            if i < len(A):
                ans = max(ans, total)

        queue = deque([(0, table[0])])

        for i in range(1, len(table)):
            ans = max(ans, table[i] - queue[0][1])
            if i >= len(A):
                while queue and queue[0][0] <= i - len(A):
                    queue.popleft()
            while queue and table[i] <= queue[-1][1]:
                queue.pop()
            queue.append((i, table[i]))
        return ans

class Solution2:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flatMax = self.findMax(A)
        cirlMax = 0
        for i in range(len(A)):
            cirlMax += A[i]
            A[i] = -A[i]
        cirlMax = cirlMax + self.findMax(A)
        if cirlMax > flatMax and cirlMax != 0:
            return cirlMax
        else:
            return flatMax

    def findMax(self, nums):
        cursum, maxsum = nums[0], nums[0]
        for n in nums[1:]:
            cursum = max(n, cursum + n)
            maxsum = max(cursum, maxsum)
        return maxsum

def main():
    A = [1, -2, 3]
    s = Solution()
    s.maxSubarraySumCircular(A)

if __name__ == '__main__':
    main()
