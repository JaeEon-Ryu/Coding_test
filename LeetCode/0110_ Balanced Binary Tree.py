'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        l_depth = self.max_depth(root.left)
        r_depth = self.max_depth(root.right)

        if abs(l_depth - r_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, root: int) -> int:
        if root is None:
            return 0

        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1