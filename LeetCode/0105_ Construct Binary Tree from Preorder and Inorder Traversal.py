'''
Given two integer arrays preorder and inorder
where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree,
construct and return the binary tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        reference : MiKueen

        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            center = inorder.index(preorder.pop(0))
            output = TreeNode(inorder[center])

            output.left = self.buildTree(preorder, inorder[:center])
            output.right = self.buildTree(preorder, inorder[center + 1:])

            return output