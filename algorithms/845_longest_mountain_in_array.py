"""
Longest Mountain in Array
-------------------------

Let's call any (contiguous) subarray B (of A) a mountain if the following
properties hold:
    - B.length >= 3
    - There exists some 0 < i < B.length - 1 such that
      B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:
    - Input: [2,1,4,7,3,2,5]
    - Output: 5
    - Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
    - Input: [2,2,2]
    - Output: 0
    - Explanation: There is no mountain.

Note:
    - 0 <= A.length <= 10000
    - 0 <= A[i] <= 10000

Follow up:
    - Can you solve it using only one pass?
    - Can you solve it in O(1) space?

Reference:
    - https://leetcode.com/problems/longest-mountain-in-array/
"""

import unittest


def longest_mountain(a):
    """
    Find longest mountain in given array

    :param a: list of numbers
    :type a: list[int]
    :return: length of longest mountain
    :rtype: int
    """
    # basic case
    length = len(a)
    if length < 3:
        return 0

    left = right = 0
    result = 0
    while left < length:
        # determine whether or not to start a mountain
        if right + 1 < length and a[right] < a[right + 1]:
            # find the ending position of ascending nubers
            while right + 1 < length and a[right] < a[right + 1]:
                right += 1
            # check whether or not current position (right) is really a peak
            if right + 1 < length and a[right] > a[right + 1]:
                # find the ending position of descending numbers
                while right + 1 < length and a[right] > a[right + 1]:
                    right += 1
                # save the length of longest mountain
                result = max(result, right - left + 1)
        # move left boundary to the next position (if mountain is not found)
        # or to the end of current mountain (if mountain is found)
        left = max(left + 1, right)
        right = left

    return result


class TestLongestMountain(unittest.TestCase):
    def test_longest_mountain(self):
        self.assertEqual(5, longest_mountain([2, 1, 4, 7, 3, 2, 5]))
        self.assertEqual(0, longest_mountain([2, 2, 2]))
        self.assertEqual(0, longest_mountain([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


if __name__ == '__main__':
    unittest.main()
