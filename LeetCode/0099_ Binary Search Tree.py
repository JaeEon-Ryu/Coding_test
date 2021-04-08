'''
You are given the root of a binary search tree (BST),
where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
풀이 방법 : 중위순회로 이진트리를 순회하면 오름차순으로 정렬된 숫자들을 볼 수 있음
여기서 오름차순으로 정렬되지 않은 숫자 두개만 뽑아서 서로 바꿔주기만 하면 됨
'''

class Solution(object):
    def recoverTree(self, root):
        """
        #reference : akshit0699
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev_node = None, None, None  # 3개의 노드 생성
        self.in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val  # 노드 값 교환

    def in_order(self, root):
        if not root:
            return

        self.in_order(root.left)

        if self.prev_node and self.prev_node.val > root.val:
            if not self.first:
                self.first = self.prev_node
            self.second = root
        self.prev_node = root

        self.in_order(root.right)