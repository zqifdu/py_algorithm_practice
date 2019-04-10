"""
https://www.lintcode.com/problem/subarray-sum-ii/description?_from=ladder&&fromId=4


"""


def subarraySumII(A, start, end):
    n = len(A)
    big_sum, small_sum = 0, 0
    big_end, small_end = 0, 0
    ans = 0
    for i in range(n):
        # Make sure small_end and big_end is at least at the current location
        small_end = max(small_end, i)
        big_end = max(big_end, i)

        # Move small_end to the right until it hits start
        while small_end < n and small_sum + A[small_end] < start:
            small_sum += A[small_end]
            small_end += 1

        # Move big_end to the right until it hits end
        while big_end < n and big_sum + A[big_end] <= end:
            big_sum += A[big_end]
            big_end += 1

        # All intermediate subarrays satisfy the condition
        if big_end - small_end > 0:
            ans += big_end - small_end

        # If small_end == i, small_sum is 0 because we haven't added anything to small_sum
        if small_end > i:
            small_sum -= A[i]

        # If big_end == i, big_sum is 0 because we haven't added anything to big_sum
        if big_end > i:
            big_sum -= A[i]

        # print(i, small_end, big_end, small_sum, big_sum)
    return ans

array = [10, 20]
start = 10
end = 20
print(subarraySumII(array, start, end))