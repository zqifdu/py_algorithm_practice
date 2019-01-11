# related LintCode:
# 1. https://www.lintcode.com/problem/sort-integers/description
# 2. https://www.lintcode.com/problem/sort-integers-ii/description


def quick_sort(nums, start, end):
    if start > end:
        return nums

    left, right = start, end
    pivot = (start + end)//2
    while left <= right:
        while nums[pivot] > nums[left] and left <= right:
            left += 1
        while nums[pivot] < nums[right] and left <= right:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    quick_sort(nums, start, right)
    quick_sort(nums, left, end)
    return nums



