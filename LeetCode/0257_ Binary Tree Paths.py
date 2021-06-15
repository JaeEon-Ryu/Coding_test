'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.dfs(root, [], True)
        return self.paths

    # 깊이 우선 탐색
    def dfs(self, root: TreeNode, path, is_in_leaf_node):
        if root.left:
            self.dfs(root.left, path + [root.val], True)
            is_in_leaf_node = False
        if root.right:
            self.dfs(root.right, path + [root.val], True)
            is_in_leaf_node = False

        if is_in_leaf_node: # 단말노드일 경우 저장
            self.paths.append(self.generator(path + [root.val]))

    # 경로에 '->' 를 추가하여 답에 저장하기 위함
    def generator(self, p):
        p = list(map(str, p))
        return '->'.join(p)

