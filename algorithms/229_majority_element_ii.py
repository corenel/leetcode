"""
Majority Element II
-------------------

Given an integer array of size n, find all elements that appear
more than n/3 times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
    - Input: [3,2,3]
    - Output: [3]

Example 2:
    - Input: [1,1,1,3,3,2,2,2]
    - Output: [1,2]

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/majority_number_ii.html
    - https://leetcode.com/problems/majority-element-ii/
    - https://www.lintcode.com/problem/majority-element-ii/
"""

import unittest
import math


def majority_element(nums):
    """
    Find the majority elements in given array

    :param nums: list[int]
    :type nums: given array of numbers
    :return: the majority elements
    :rtype: list[int]
    """
    if len(nums) == 0:
        return []

    k1, k2, c1, c2 = math.inf, math.inf, 0, 0
    for n in nums:
        if c1 == 0 and k1 != n and k2 != n:
            k1 = n
        elif c2 == 0 and k2 != n and k1 != n:
            k2 = n

        if k1 == n:
            c1 += 1
        elif k2 == n:
            c2 += 1
        else:
            c1 -= 1
            c2 -= 1

    c1, c2 = 0, 0
    for n in nums:
        if n == k1:
            c1 += 1
        elif n == k2:
            c2 += 1
    if c1 <= len(nums) // 3:
        k1 = math.inf
    if c2 <= len(nums) // 3:
        k2 = math.inf

    return [k for k in (k1, k2) if not math.isinf(k)]


class TestMajorityElementII(unittest.TestCase):
    def test_majority_element_ii(self):
        self.assertEqual([3], majority_element([3, 2, 3]))
        self.assertEqual([1, 2], majority_element([1, 1, 1, 3, 3, 2, 2, 2]))
        self.assertEqual([-1], majority_element([0, -1, 2, -1]))
        self.assertEqual([1, 2], majority_element([1, 2, 2, 3, 2, 1, 1, 3]))


if __name__ == '__main__':
    unittest.main()
