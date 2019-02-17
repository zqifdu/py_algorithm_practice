"""
Find the sum of contiguous subarray within an array of numbers which has the largest sum.

Return an integer representing the largest sum

Examples:
------
Input: [-2, 4, -1, -2, 1, 5, -3, -15, 2, 3]
Output: 7 # The largest sum is within the subarray [ 4, -1, -2, 1, 5]

Input: [1 ,4 ,6, 21]
Output: 32 # The largest sum is all numbers in the array because they are all positive

"""


# Dynamic programming solution
# Time complexity: O(n^2)
# Space complextiy: O(n^2)
def largestSumSubarray(A):
    max_sum = 0
    # sum from index i to index j
    sum_ij = [[0]*len(A) for _ in range(len(A))]

    for i in range(len(A)):
        sum_ij[i][i] = A[i]
        max_sum = max(max_sum, sum_ij[i][i])

    for k in range(1, len(A)):
        for j in range(k, len(A)):
            i = j - k
            sum_ij[i][j] = sum_ij[i+1][j] + A[i]
            # print(i, j, sum_ij[i][j])
            max_sum = max(max_sum, sum_ij[i][j])

    return max_sum


# Sliding window solution
# Time complexity: O(n)
# Space complexity: O(1)
def largestSumSubarray_sw(A):
    if not A:
        return 0
    if len(A) == 1:
        return A[0]

    right = 1
    subtotal = A[0]
    max_sum = max(0, subtotal)
    while right < len(A):
        while subtotal >= 0 and right < len(A):
            subtotal += A[right]
            max_sum = max(max_sum, subtotal)
            right += 1

        subtotal = 0

    return max_sum


def largestSumSubarray_sw2(A):
    max_so_far = float('-inf')
    curr_sum = 0
    for i in range(0, len(A)):
        curr_sum += A[i]
        if max_so_far < curr_sum:
            max_so_far = curr_sum

        if curr_sum < 0:
            curr_sum = 0

A = [-2, 4, -1, -2, 1, 5, -3, -15, 2, 3]
assert largestSumSubarray_sw(A) == 7
A = [-10, -20]
assert largestSumSubarray_sw(A) == 0
A = [10, -20]
assert largestSumSubarray_sw(A) == 10
A = []
assert largestSumSubarray_sw(A) == 0

