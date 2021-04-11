'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.output = []
        if root:
            self.preorder_traversal(root, 1)

        result = []
        for idx, sub in enumerate(self.output): # 지그재그를 위해 
            if idx % 2 == 0:
                result.append(sub)
            else:
                result.append(sub[::-1])

        return result

    def preorder_traversal(self, root: TreeNode, level): # 전위순회
        if len(self.output) < level:
            self.output.append([root.val])
        else:
            self.output[level - 1].append(root.val)

        if root.left:
            self.preorder_traversal(root.left, level + 1)
        if root.right:
            self.preorder_traversal(root.right, level + 1)