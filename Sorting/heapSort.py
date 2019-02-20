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


def heapify_iter(A, start, end):
    '''
    Iterative version of heapify
    :param A:       number list
    :param start:   Heapify the tree starting from index start
    :param end:     Heapify the tree ending with index end
    :return:
    '''
    curr = start

    while curr < end:
        left, right = 2 * curr + 1, 2 * curr + 2
        mx = A[curr]
        if left < end and A[left] > mx:
            mx = A[left]
            new_mx = left
        if right < end and A[right] > mx:
            mx = A[right]
            new_mx = right
        if mx != A[curr]:
            A[curr], A[new_mx] = A[new_mx], A[curr]
            curr = new_mx
        else:
            break