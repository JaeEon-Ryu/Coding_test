'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check_symmetric(root, root)

    def check_symmetric(self, root_1: TreeNode, root_2: TreeNode) -> bool:
        if not root_1 and not root_2:
            return True
        if not root_1 or not root_2: # 한쪽만 값이 있는 경우
            return False

        return root_1.val == root_2.val and \
               self.check_symmetric(root_1.left, root_2.right) and \
               self.check_symmetric(root_1.right, root_2.left)