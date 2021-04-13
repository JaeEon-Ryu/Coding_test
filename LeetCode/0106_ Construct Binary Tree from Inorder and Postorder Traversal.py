'''
Given two integer arrays inorder and postorder
where inorder is the inorder traversal of a binary tree and
postorder is the postorder traversal of the same tree,
construct and return the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # reference : OldCodingFarmer
    def buildTree(self, inorder, postorder):
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder)  # left부터 실행 시 인덱스 에러
            root.left = self.buildTree(inorder[:idx], postorder)
            return root
