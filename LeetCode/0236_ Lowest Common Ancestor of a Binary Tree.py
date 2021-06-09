'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.target = [p.val, q.val]
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return None

        if root.val in self.target:
            return root

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root