'''
Given the root of a binary tree,
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.output = []
        if root:
            self.preorder_traversal(root, 1)
        return self.output

    def preorder_traversal(self, root: TreeNode, level):
        if len(self.output) < level: # 레벨에 해당하는 리스트가 없다면
            self.output.append([root.val])
        else:
            self.output[level - 1].append(root.val)

        if root.left:
            self.preorder_traversal(root.left, level + 1)
        if root.right:
            self.preorder_traversal(root.right, level + 1)
