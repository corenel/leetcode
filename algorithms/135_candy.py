"""
Candy
-----

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following
requirements:

    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example 1:
    - Input: [1,0,2]
    - Output: 5
    - Explanation: You can allocate to the first, second and third child
      with 2, 1, 2 candies respectively.

Example 2:
    - Input: [1,2,2]
    - Output: 4
    - Explanation: You can allocate to the first, second and third child
      with 1, 2, 1 candies respectively. The third child gets 1 candy because
      it satisfies the above two conditions.

Reference:
    - https://www.codingeek.com/practice-examples/interview-programming-problems/minimum-candy-distribution-interview-algorithm-problem/
    - https://leetcode.com/problems/candy/
"""

import unittest


def candy(ratings):
    """
    Candy distribution

    :param ratings: list of ratings
    :type ratings: list[int]
    :return: minimum number of candies to give
    :rtype: int
    """
    candies = [1] * len(ratings)
    for i in range(len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            candies[i + 1] = candies[i] + 1
    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
            candies[i - 1] = candies[i] + 1
    return sum(candies)


def candy_circle(ratings):
    """
    Candy distribution for circle (0th and (n-1)th are adjacent)

    :param ratings: list of ratings
    :type ratings: list[int]
    :return: minimum number of candies to give
    :rtype: int
    """
    candies = [1] * len(ratings)
    for i in range(len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            candies[i + 1] = candies[i] + 1
    for i in range(0, -len(ratings) + 1, -1):
        if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
            candies[i - 1] = candies[i] + 1
    return sum(candies)


class TestCandy(unittest.TestCase):
    def test_candy(self):
        self.assertEqual(5, candy([1, 0, 2]))
        self.assertEqual(4, candy([1, 2, 2]))
        self.assertEqual(11, candy([1, 3, 4, 5, 2]))

    def test_candy_circle(self):
        self.assertEqual(3, candy_circle([1, 2]))
        self.assertEqual(8, candy_circle([1, 2, 3, 3]))


if __name__ == '__main__':
    unittest.main()
