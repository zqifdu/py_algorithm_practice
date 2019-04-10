"""
Lintcode 15: Permutaitons
https://www.lintcode.com/problem/permutations/description?_from=ladder&&fromId=1
"""


def permute(nums):
    if nums is None:
        return []
    if nums == []:
        return [[]]
    nums = sorted(nums)
    permutation = []
    stack = [-1]
    permutations = []

    while len(stack):
        index = stack.pop()
        index += 1
        while index < len(nums):
            if nums[index] not in permutation:
                break
            index += 1
        else:
            if len(permutation):
                permutation.pop()
            continue

        stack.append(index)
        stack.append(-1)
        permutation.append(nums[index])
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
    return permutations


nums = [1, 2, 3]
print(permute(nums))