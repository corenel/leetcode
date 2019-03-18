"""
Peak Index in a Mountain Array
------------------------------

Let's call an array A a mountain if the following properties hold:

    - A.length >= 3
    - There exists some 0 < i < A.length - 1 such that
      A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
    - Input: [0,1,0]
    - Output: 1

Example 2:
    - Input: [0,2,1,0]
    - Output: 1

Note:
    - 3 <= A.length <= 10000
    - 0 <= A[i] <= 10^6
    - A is a mountain, as defined above.
"""

import unittest


def peak_index_in_mountain_array(a):
    """
    Find peak index of mountain in given array

    :param a: list of numbers
    :type a: list[int]
    :return: peak index of
    :rtype: int
    """
    # basic case
    if len(a) < 3:
        return 0

    # find peak index
    left, right = 1, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid - 1] < a[mid] and a[mid] > a[mid + 1]:
            return mid
        elif a[mid - 1] < a[mid] < a[mid + 1]:
            left = mid + 1
        elif a[mid - 1] > a[mid] > a[mid + 1]:
            right = mid - 1
        else:
            left += 1

    return 0


class TestPeakIndexInAMountainArray(unittest.TestCase):
    def test_peak_index_in_a_mountain_array(self):
        self.assertEqual(1, peak_index_in_mountain_array([0, 1, 0]))
        self.assertEqual(1, peak_index_in_mountain_array([0, 2, 1, 0]))
        self.assertEqual(0, peak_index_in_mountain_array([0, 2, 2, 1, 0]))


if __name__ == '__main__':
    unittest.main()
