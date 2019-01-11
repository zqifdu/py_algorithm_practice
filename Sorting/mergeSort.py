"""
Merge sort python implementation

related LintCode:
1. https://www.lintcode.com/problem/sort-integers/description
2. https://www.lintcode.com/problem/sort-integers-ii/description
"""



def merge_sort(nums, start, end, temp):
    if start > end or end - start <= 1:
        return nums

    m = (start + end)//2
    merge_sort(nums, start, m, temp)
    merge_sort(nums, m, end, temp)

    # merging two parts
    left, right = start, m
    temp_ind = start
    while temp_ind < end:
        if left >= m:
            temp[temp_ind] = nums[right]
            right += 1
        elif right >= end:
            temp[temp_ind] = nums[left]
            left += 1
        elif nums[left] <= nums[right]:
            temp[temp_ind] = nums[left]
            left += 1
        else:
            temp[temp_ind] = nums[right]
            right += 1
        temp_ind += 1

    for i in range(start, end):
        nums[i] = temp[i]
    return nums