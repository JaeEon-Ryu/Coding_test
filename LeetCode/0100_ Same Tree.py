'''
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same
if they are structurally identical, and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True

        self.is_same = True
        self.pre_order_search(p, q)

        return self.is_same

    def pre_order_search(self, p, q):

        if not self.is_same:
            return

        # 이진트리의 크기가 서로 다른 경우
        if ((p and not q) or (not p and q)) or ((p.left and not q.left) or (not p.left and q.left)) or (
                (p.right and not p.right) or (not p.right and q.right)):
            self.is_same = False
            return

        # 값이 서로 다른 경우
        if p and q:
            if p.val != q.val:
                self.is_same = False
                return

        # 분기
        if p.left and q.left:
            self.pre_order_search(p.left, q.left)

        if q.right and q.right:
            self.pre_order_search(p.right, q.right)

