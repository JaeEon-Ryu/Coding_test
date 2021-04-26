'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS 방식으로 구현
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.nums = []
        self.generator(root, str(root.val))

        return sum(self.nums)

    def generator(self, node: TreeNode, current_num):
        if not node.left and not node.right: # 단말노드일 경우
            self.nums.append(int(current_num))
            return

        if node.left:
            self.generator(node.left, current_num + str(node.left.val))
        if node.right:
            self.generator(node.right, current_num + str(node.right.val))