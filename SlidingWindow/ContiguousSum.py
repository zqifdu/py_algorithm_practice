"""
Given an array of unsorted integers and a integer target, return true
if a contiguous subarray sums up to the integer target. Otherwise, return
False
"""


# contiguous sum
# Time complexity: O(n^2)
def contiguousArraySum(A, target):
    pre_sum = [0] * (len(A) + 1)

    for i, a in enumerate(A):
        pre_sum[i + 1] = pre_sum[i] + a
        if pre_sum[i + 1] == target:
            return True
        for j in range(i):
            if target == pre_sum[i + 1] - pre_sum[j + 1]:
                return True
    return False

# set to do the search
# Time complexity: O(n)
# Space complexity: O(n)
def containsTotalSet(A, target):
    sums = set()
    s = 0
    for x in A:
        s += x
        if (s - target) in sums:
            return True

    return False


print(contiguousArraySum([3, 1, 1], 2))
print(contiguousArraySum([3, 2, 0, 1], 0))


# Time complexity: O(n)
# Space complexity: O(1)
def contiguousArraySum_slidingWindow(A, target):
    # Only works when the numbers are all positives or 0
    if not A:
        return False
    left, right = 0, 0
    curr_sum = sum(A[left:right])
    while left < len(A) and right < len(A):
        if curr_sum < target:
            right += 1
            if right < len(A):
                curr_sum += A[right]
        elif curr_sum > target:
            left += 1
            if left < len(A):
                curr_sum -= A[left - 1]

        if curr_sum == target:
            return True

    return False


def contiguousArraySum_slidingWindow(A, target):
    start = end = 0
    subtotal = 0
    while end < len(A):
        subtotal += A[end]
        end += 1

        while subtotal > target and start < end - 1:
            subtotal -= A[start]
            start += 1

        if subtotal == target:
            return True
    return False


print(contiguousArraySum_slidingWindow([3, 2, 1], 4))