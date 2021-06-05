'''
Given the root of a binary search tree, and an integer k,
return the kth (1-indexed) smallest element in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
왼쪽 노드를 쭉 타고 들어가서 다시 중위순회식으로 올라오다보면 정렬 순서임
'''

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.smallest = None
        self.k, self.cnt = k, 0
        self.dfs(root)

        return self.smallest

    def dfs(self, root: TreeNode):
        if root.left:
            self.dfs(root.left)

        self.cnt += 1

        if self.cnt == self.k:
            self.smallest = root.val
            return

        if root.right:
            self.dfs(root.right)
