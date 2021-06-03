'''
Given the root of a binary tree, invert the tree, and return its root.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        new_tree = TreeNode(root.val)
        self.dfs(root, new_tree)

        return new_tree

    def dfs(self, root: TreeNode, new_root: TreeNode):
        if root.left:
            new_root.right = TreeNode(root.left.val)
            self.dfs(root.left, new_root.right)
        if root.right:
            new_root.left = TreeNode(root.right.val)
            self.dfs(root.right, new_root.left)


    '''
    새로운 tree를 만들지 않고 값만 바꾸는 경우
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            # General case:
            
            # invert child node of current root
            root.left, root.right = root.right, root.left
            
            # invert subtree with DFS
            
            if root.left:
                self.invertTree( root.left )
            
            if root.right:
                self.invertTree( root.right )
            
            return root
        
        else:
            # Base case:
            # empty tree
            
            return None
    '''