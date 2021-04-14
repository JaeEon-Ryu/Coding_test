'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
수정해야함
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.depths = []
        self.find_depth(root, 0)

        depths = sorted(list(set(self.depths)))
        if depths:
            temp = depths[0]
            for i in range(1,len(depths)-1):
                if depths[i] - temp > 1:
                    return False
                temp = depths[i]

        return True

    def find_depth(self, root: TreeNode, depth):
        if not root:
            self.depths.append(depth)
            return

        self.find_depth(root.left, depth + 1)
        self.find_depth(root.right, depth + 1)


