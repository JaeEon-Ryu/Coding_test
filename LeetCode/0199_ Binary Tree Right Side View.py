'''
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.result = {}
        self.dfs(root, 0)
        return [self.result[i] for i in range(len(self.result))]

    def dfs(self, root: TreeNode, level: int):
        if not root:
            return

        self.dfs(root.right, level + 1)
        if level not in self.result:
            self.result[level] = root.val
        self.dfs(root.left, level + 1)
