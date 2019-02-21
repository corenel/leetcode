"""
Group Anagrams
--------------

Given an array of strings, group anagrams together.

LeetCode Example:

- Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
- Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

Note:

- All inputs will be in lowercase.
- The order of your output does not matter.
"""

import unittest


def group_anagrams(strs):
    """
    Group anagrams in given list of strings

    :param strs: a list of input strings
    :type strs: list[str]
    :return: grouped anagrams
    :rtype: list[str]
    """
    str_dict = {}
    for string in strs:
        str_sorted = ''.join(sorted(string))
        if str_sorted not in str_dict:
            str_dict[str_sorted] = [string]
        else:
            str_dict[str_sorted].append(string)
    return list(str_dict.values())


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams_leetcode(self):
        self.assertListEqual(
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
            group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))


if __name__ == '__main__':
    unittest.main()
