"""
Binary Tree Postorder Traversal
-------------------------------

Given a binary tree, return the postorder traversal of its nodes' values.

Example:
    - Input:
        1
         \
          2
         /
        3
    - Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/binary_tree_postorder_traversal.html
    - https://leetcode.com/problems/binary-tree-postorder-traversal/
    - https://www.lintcode.com/problem/binary-tree-postorder-traversal/
"""

import unittest

from utils import TreeNode


def postorder_traversal_recursive(root):
    """
    Return the postorder traversal of nodes' values.

    - Worst Time complexity: O(n)
    - Worst Space complexity: O(n)

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: postorder traversal of nodes' values
    :rtype: list[int]
    """
    # basic case
    if root is None:
        return []

    # inorder traversal: left + root + right
    left = postorder_traversal_recursive(root.left)
    right = postorder_traversal_recursive(root.right)

    return left + right + [root.val]


def postorder_traversal_iterative(root):
    """
    Return the postorder traversal of nodes' values.

    - Worst Time complexity: O(n)
    - Worst Space complexity: O(n)

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: postorder traversal of nodes' values
    :rtype: list[int]
    """
    # basic case
    if root is None:
        return []

    # use stack to traverse
    result = []
    stack = [root]
    prev = None
    while len(stack) != 0:
        curr = stack[-1]
        no_child = curr.left is None and curr.right is None
        child_visited = prev is not None and \
                        (curr.left == prev or curr.right == prev)
        if no_child or child_visited:
            result.append(curr.val)
            stack.pop()
            prev = curr
        else:
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)

    return result


class TestPostorderTraversal(unittest.TestCase):
    def test_postorder_traversal(self):
        # 1
        #  \
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertListEqual([3, 2, 1], postorder_traversal_recursive(root))
        self.assertListEqual([3, 2, 1], postorder_traversal_iterative(root))


if __name__ == '__main__':
    unittest.main()
