'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        result = []

        def generator(root, result):
            if root != None:
                if root.left != None:
                    generator(root.left, result)
                result.append(root.val)
                if root.right != None:
                    generator(root.right, result)

        generator(root, result)
        return result