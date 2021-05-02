'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        if root:
            self.dfs(root)
        return self.result

    def dfs(self, root: TreeNode):
        self.result.append(root.val)
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)