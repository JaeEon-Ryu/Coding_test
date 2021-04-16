'''
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        self.target_found = False
        self.targetSum = targetSum
        self.search(root, 0)

        return self.target_found

    def search(self, root: TreeNode, path_sum: int):
        if self.target_found:
            return

        path_sum += root.val  # 현재 경로의 합 누적

        if not root.left and not root.right:  # 자식노드가 없다면 경로 합 비교
            if path_sum == self.targetSum:
                self.target_found = True
                return

        if root.left:
            self.search(root.left, path_sum)
        if root.right:
            self.search(root.right, path_sum)
