'''
Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.results = []
        self.targetSum = targetSum
        self.search(root, [])

        return self.results

    def search(self, root: TreeNode, path: List[int]):
        path.append(root.val) # 현재 경로의 값 리스트에 누적

        if not root.left and not root.right: # 자식 노드가 없다면 합 비교
            if sum(path) == self.targetSum:
                self.results.append(list(path))

        if root.left:
            self.search(root.left, path)
        if root.right:
            self.search(root.right, path)

        path.pop()