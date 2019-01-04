# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing
# sequence by removing no more than one element from the array.
# -----------
# Example:
#
# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false.
#
# There is no one element in this array that can be removed in order to get a strictly increasing sequence.
#
# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.
#
# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
# -----------
# Input/Output
#
# [execution time limit] 4 seconds (py3)
# -----------
# [input] array.integer sequence
#
# Guaranteed constraints:
# 2 ≤ sequence.length ≤ 105,
# -105 ≤ sequence[i] ≤ 105.
# -----------
# [output] boolean
#
# Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.


def almost_increase(nums):
    nums = [-float('inf')] + nums
    one_deleted = False
    i = 2
    while i < len(nums):
        if nums[i] <= nums[i-1] and not one_deleted:
            if nums[i] <= nums[i-2]:
                nums.pop(i)     # delete the new number
            elif nums[i] > nums[i-2]:
                nums.pop(i-1)   # delete last number
            one_deleted = True
        elif nums[i] <= nums[i-1] and one_deleted:
            return False
        else:
            # Move forward
            i += 1
    return True


# test cases:
nums = []
assert almost_increase(nums) is True

nums = [1, 3, 2]
assert almost_increase(nums) is True

nums = [1, 3, 2, 1]
assert almost_increase(nums) is False

nums = [2, 4, 3, 4]
assert almost_increase(nums) is True

nums = [2, 4, 1, 4]
assert almost_increase(nums) is False

nums = [10, 1, 2, 3]
assert almost_increase(nums) is True

nums = [9, 10, 1, 2, 3]
assert almost_increase(nums) is False

nums = [1, 2, 3, 4, 3, 6]
assert almost_increase(nums) is True
print(almost_increase(nums))





