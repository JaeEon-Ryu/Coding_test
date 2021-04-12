'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.Output = 0

        if root:
            self.preorder_traversal(root, 1)

        return self.Output

    def preorder_traversal(self, root: TreeNode, depth: int):
        self.Output = max(self.Output, depth)

        if root.left:
            self.preorder_traversal(root.left, depth + 1)
        if root.right:
            self.preorder_traversal(root.right, depth + 1)

'''
다른 사람의 풀이 - StefanPochmann # map함수 활용

def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
'''