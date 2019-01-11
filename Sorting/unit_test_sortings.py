"""
Unittest the sorting algorithms
"""

import unittest
from Sorting.quickSort import *
from Sorting.mergeSort import *


class UnittestSorting(unittest.TestCase):
    def setUp(self):
        self.testcases = []
        self.testcases.append([])
        self.testcases.append([1])
        self.testcases.append([1, 2, 3])
        self.testcases.append([3, 2, 1])
        self.testcases.append([1, 1, 2])
        self.testcases.append([2, 2, 1])
        self.testcases.append([2, 2, 2])
        self.testcases.append([1, 24, 98, 27, 18, 89, 77])

    def test_quickSort(self):
        for nums in self.testcases:
            print('Sorting', nums)
            if quick_sort(nums, 0, len(nums) - 1) != sorted(nums):
                print(quick_sort(nums, 0, len(nums) - 1))
                print('Wrong result for test case', nums)
                print('Expected', sorted(nums))

    def test_mergeSort(self):
        for nums in self.testcases:
            if merge_sort(nums, 0, len(nums), [0]*len(nums)) != sorted(nums):
                print(merge_sort(nums, 0, len(nums), [0]*len(nums)))
                print('Wrong result for test case', nums)
                print('Expected', sorted(nums))