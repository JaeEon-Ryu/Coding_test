'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
bottom-up 방식으로 풀이
'''

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = -1000
        self.generator(root)

        return self.max

    def generator(self, node: TreeNode):
        if not node:
            return 0

        left = self.generator(node.left)
        right = self.generator(node.right)
        self.max = max(self.max, left + node.val + right)

        return max(node.val + max(left, right), 0)
