"""
Heap sort python implementation

related LintCode:
1. https://www.lintcode.com/problem/sort-integers/description
2. https://www.lintcode.com/problem/sort-integers-ii/description
"""


def heap_sort(nums):
    build_max_heap(nums)
    print('after build the max heap, ', nums)
    for i in range(len(nums) - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)

    return nums


def build_max_heap(nums):
    n = len(nums)
    for i in range(n//2, -1, -1):
        heapify(nums, i, n)


def heapify(nums, i, end):
    max = i
    left, right = 2*i + 1, 2*i + 2
    if left < end and nums[i] < nums[left]:
        max = left

    if right < end and nums[max] < nums[right]:
        max = right

    if i != max:
        nums[max], nums[i] = nums[i], nums[max]
        heapify(nums, max, end)

