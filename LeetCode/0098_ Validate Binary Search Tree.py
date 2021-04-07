'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
왼쪽으로 갈 경우  -> 상위최소노드 < root.left < root.val 
                 -> 상위 최대 노드 값 갱신

오른쪽으로 갈 경우 -> root.val < root.right < 상위최대노드
                 -> 상위 최소 노드 값 갱신
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        global is_valid
        is_valid = True

        def recursive_search(higher_min_root, higher_max_root, current_root):
            global is_valid
            if not is_valid:
                return

            if current_root.left != None and current_root.left.val != 'null':
                if higher_min_root < current_root.left.val < current_root.val:
                    recursive_search(higher_min_root, current_root.val, current_root.left)
                else:
                    is_valid = False
                    return

            if current_root.right != None and current_root.right.val != 'null':
                if current_root.val < current_root.right.val < higher_max_root:
                    recursive_search(current_root.val, higher_max_root, current_root.right)
                else:
                    is_valid = False
                    return

        recursive_search(-2 ** 31 - 1, 2 ** 31, root)

        return is_valid


