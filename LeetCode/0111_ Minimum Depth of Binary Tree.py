'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.min_depth = 100000
        self.depth_search(root, 1)
        return self.min_depth

    def depth_search(self, root: TreeNode, depth: int):
        if not root.left and not root.right: # 단말노드의 조건 : left,right 자식노드가 없는 것
            self.min_depth = min(self.min_depth, depth)
            return

        if root.left:
            self.depth_search(root.left, depth + 1)
        if root.right:
            self.depth_search(root.right, depth + 1)


